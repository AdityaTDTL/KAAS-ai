from app.recommendation.personalized_recommender import personalized_recommendation
from app.recommendation.history import get_learning_history
from app.recommendation.recommender import users
from app.recommendation.groq_explainer import generate_explanation

def ai_recommendation(user_id):
    user = users[
        users["user_id"] == user_id
    ]

    user_profile = user.iloc[0].to_dict()

    history = get_learning_history(
        user_id
    )

    courses = personalized_recommendation(
        user_id
    )

    explanation = generate_explanation(
        user_profile,
        history,
        courses
    )

    return {
        "user_id":user_id,
        "recommended_courses":courses,
        "ai_explanation": explanation
    }
