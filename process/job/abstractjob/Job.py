from typing import Any


class Job():
    def __init__(self, name_job, function, args, args_getter=None):
        self.name_job = name_job
        self.function = function
        self.result_flag = bool
        self.job_result = Any
        self.args = args
        self.args_getter = args_getter

    def get_job_result(self):
        return self.job_result

    def run(self, job_number: int) -> {bool, Any}:
        if self.args_getter:
            self.args = self.args_getter()
        self.result_flag = True
        print("[Job #{}]-({}) running...".format(job_number, self.name_job))
        try:
            self.job_result = self.function(self.args)
        except Exception as e:
            self.result_flag = False
            print("[Job #{}]-({}) error: {}".format(job_number, self.name_job, e))

        return self.result_flag, self.job_result
