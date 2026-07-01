# agents/action.py


from .mentor_agent import generate_mentor_response



def execute_action(action, learner):


    if action == "EXPLAIN_TOPIC":


        return generate_mentor_response(
            learner,
            "Learner has low understanding"
        )



    elif action == "PROVIDE_ALTERNATIVE_EXPLANATION":


        return generate_mentor_response(
            learner,
            "Learner needs another explanation"
        )



    elif action == "SEND_REMINDER":


        return {

            "message":
            "Continue your learning journey."

        }



    return {

        "message":
        "No action needed"

    }