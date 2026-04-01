def evaluate_condition(condition, data):
    try:
        return eval(condition, {}, data)
    except:
        return False