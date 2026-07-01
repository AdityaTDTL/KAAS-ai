# agents/mentor_agent.py



def generate_mentor_response(learner, problem):


    return {

        "mentor_message":

        f"""
Hello learner.

I noticed:
{problem}

Topic:
{learner.get('topic')}

Let's learn this concept with a simpler explanation.

"""

    }