from typing import Any


class Job():
    def __init__(self, name_job, function, args):
        self.name_job = name_job
        self.function = function
        self.result_flag = bool
        self.job_result = Any
        self.args = args

    def run(self, job_number: int) -> {bool, Any}:
        self.result_flag = True
        print("[Job #{}]-({}) running...".format(job_number, self.name_job))
        try:
            self.job_result = self.function(self.args)
        except Exception as e:
            self.result_flag = False
            print("[Job #{}]-({}) error: {}".format(job_number, self.name_job, e))

        return self.result_flag, self.job_result
