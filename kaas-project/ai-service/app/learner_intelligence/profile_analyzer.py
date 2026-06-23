from app.database.queries import get_user_profile

def analyze_learner(user_id):
    profile = get_user_profile(user_id)

    if not profile:
        return {
            "error": "User not found"
        }

    user = profile[0]

    learner_context = {
        "user_id": user["user_id"],
        "name": (
            user["first_name"]
            + " "
            + user["last_name"]
        ),
        "role": user["role"],
        "domain_interest": user["primary_domain_interest"],
        "current_level": user["current_level"],
        "career_goal": user["career_goal"],
        "learning_style": user["learning_style"]
    }

    return learner_context
