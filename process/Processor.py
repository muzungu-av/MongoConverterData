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
        job_1: Job
        if self.reader.read_collection(self.reader, Collection=self.source_coll) == True:
            # job 1 - find one collection
            function = lambda t: list(self.reader.get_collection(self.reader).find(t[0], t[1]))
            from process.job.jobparam.job1_filter_param import job1f
            job_1: Job = Job("find all coll",
                             function,
                             ({}, {}))
            self.jobs.append(job_1)

            # job 2 - write collection
            coll_1 = self.writer.set_collection(self.writer, Collection=self.target_coll_1)
            function = lambda t: coll_1.insert_many(t)
            job_2: Job = Job("insert_into collection {}".format(self.target_coll_1), function,
                             (), job_1.get_job_result)
            self.jobs.append(job_2)

            # # job 3 - write collection
            coll_2 = self.writer.set_collection(self.writer, Collection=self.target_coll_2)
            function = lambda t: coll_2.insert_many(t)
            job_3: Job = Job("insert_into collection {}".format(self.target_coll_2), function,
                             (), job_1.get_job_result)
            self.jobs.append(job_3)

            # job 3 - insert one collection
            # coll = self.writer.set_collection(self.writer, Collection=self.target_coll_1)
            # d = {"_id": 5, "name": "Raju", "Roll No": "1005", "Branch": "CSE"}
            # function = lambda t: coll.insert_one(t)
            # job_3: Job = Job("insert one doc", function, (d))
            # self.jobs.append(job_3)



            self.run_jobs()

    def run_jobs(self):
        import pymongo
        result_flag: bool
        job_number: int = 1
        while self.jobs:
            job = self.jobs.pop(0)
            result_flag, self.job_result = job.run(job_number)

            ## prints
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
