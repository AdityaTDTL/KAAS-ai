# agents/decision_engine.py


def decide_action(problems):

    if "LOW_SCORE" in problems:

        return "EXPLAIN_TOPIC"


    if "REPEATED_CONTENT" in problems:

        return "PROVIDE_ALTERNATIVE_EXPLANATION"


    if "INACTIVE" in problems:

        return "SEND_REMINDER"


    return "NO_ACTION"