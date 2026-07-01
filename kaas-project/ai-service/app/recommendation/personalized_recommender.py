from app.recommendation.recommender import users, courses
from app.recommendation.history import get_learning_history

def personalized_recommendation(user_id):
    user = users[
        users["user_id"] == user_id
    ]

    if user.empty:
        return {
            "error":"User not found"
        }

    user = user.iloc[0]

    history = get_learning_history(user_id)

    domain = user["primary_domain_interest"]
    level = user["current_level"]

    recommended = courses[
        (courses["domain"] == domain)
        &
        (courses["level"] == level)
        &
        (courses["status"] == "Published")
    ]

    completed = history["completed_courses"]
    learning = history["in_progress_courses"]

    recommended = recommended[
        ~recommended["course_id"].isin(
            completed + learning
        )
    ]

    return recommended.head(5).to_dict(
        orient="records"
    )
