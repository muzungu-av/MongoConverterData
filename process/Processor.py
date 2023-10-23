from factory.read.Reader import Reader
from factory.write.Writer import Writer
from process.job.abstractjob.Job import Job


class Processor():
    def __init__(self, reader: Reader, writer: Writer):
        self.reader = reader
        self.writer = writer
        self.source_coll = "hydrus_ghgemissions"
        self.target_coll_1 = "hydrus_calculation_items"
        self.target_coll_2 = "hydrus_calculations"
        self.job_result = None
        self.jobs = list()

    def process(self):
        if self.reader.read_collection(self.reader, Collection=self.source_coll) == True:
            # job 1 - find one collection
            function = lambda t: self.reader.get_collection(self.reader).find_one()
            job_1: Job = Job("find one", function, ())
            self.jobs.append(job_1)

            # job 2 - find all collection
            function = lambda t: self.reader.get_collection(self.reader).find(t[0], t[1])
            job_2: Job = Job("find all coll",
                             function,
                             ({}, {"_id": 1, "name": 1, "description": 1, "date_start": 1, "date_end": 1, "regions": 1}))
            self.jobs.append(job_2)

            # job 3 - insert one collection
            coll = self.writer.set_collection(self.writer, Collection=self.target_coll_1)
            d = {"_id": 5, "name": "Raju", "Roll No": "1005", "Branch": "CSE"}
            function = lambda t: coll.insert_one(d)
            job_3: Job = Job("insert one doc", function, ())
            self.jobs.append(job_3)

            # job 4 - write collection
            # coll = self.writer.set_collection(self.writer, Collection=self.target_coll_1)
            # print(self.job_result)
            # function = lambda t: coll.insert_many(d)
            # job_4: Job = Job("insert one doc", function, ())
            # self.jobs.append(job_4)

            self.run_jobs()

    def run_jobs(self):
        import pymongo
        result_flag: bool
        job_number: int = 1
        while self.jobs:
            job = self.jobs.pop(0)
            result_flag, self.job_result = job.run(job_number)

            # print result
            if result_flag == False:
                print("[Processor]- Job #{} ({}) failed, job_result: {}".format(job_number, job.name_job,
                                                                                self.job_result))
                print("[Processor]- Job #{} processing has stopped".format(job_number))
                break
            else:
                if (isinstance(self.job_result, (pymongo.cursor.Cursor))):
                    for doc in self.job_result:
                        print("[Processor]- Job #{} has successfully processed the document id='{}' name='{}'".format(
                            job_number, doc["_id"], doc["name"]))
                elif (isinstance(self.job_result, (dict))):
                    print("[Processor]- Job #{} has successfully processed the document id='{}' name='{}'".format(
                        job_number, self.job_result["_id"], self.job_result["name"]))

                job_number += 1

        print("[Processor]- Jobs processing has finished")
