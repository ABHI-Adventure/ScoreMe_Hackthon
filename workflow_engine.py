import json
import random
import time

class WorkflowEngine:

    def __init__(self):
        with open("config/workflow.json") as f:
            self.workflow = json.load(f)

    def execute(self, request_type):
        steps = self.workflow.get(request_type, [])

        for step in steps:
            # simulate external dependency failure
            if step == "RULE_CHECK":
                if random.choice([True, False]):
                    time.sleep(1)
                else:
                    raise Exception("External API Failure")

        return True