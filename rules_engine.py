import json
from utils import evaluate_condition

class RulesEngine:

    def __init__(self):
        with open("config/rules.json") as f:
            self.rules = json.load(f)

    def evaluate(self, request_type, data):
        logs = []
        decision = "APPROVED"

        for rule in self.rules.get(request_type, []):
            result = evaluate_condition(rule["condition"], data)

            logs.append({
                "rule": rule["name"],
                "result": "PASS" if result else "FAIL"
            })

            if not result:
                decision = rule["fail_action"]
                return decision, logs

        return decision, logs