from .decision_engine import decide_action
from .action import execute_action



def run_ai_agent(learner):


    problems = []


    # Detect learning problems

    if learner["quiz_score"] < 50:

        problems.append(
            "LOW_SCORE"
        )


    if learner["video_views"] > 2:

        problems.append(
            "REPEATED_CONTENT"
        )


    if learner["days_inactive"] > 7:

        problems.append(
            "INACTIVE"
        )


    # Agent decision

    action = decide_action(
        problems
    )


    # Perform action

    result = execute_action(
        action,
        learner
    )


    return {

        "detected_problems": problems,

        "action": action,

        "result": result

    }