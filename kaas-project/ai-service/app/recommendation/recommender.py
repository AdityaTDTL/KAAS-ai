import pandas as pd
import os

# Using absolute paths or correctly relative paths based on project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
USERS_PATH = os.path.join(BASE_DIR, "data", "datasets", "users.csv")
COURSES_PATH = os.path.join(BASE_DIR, "data", "datasets", "courses.csv")
ENROLLMENTS_PATH = os.path.join(BASE_DIR, "data", "datasets", "enrollments.csv")

users = pd.read_csv(USERS_PATH)
courses = pd.read_csv(COURSES_PATH)
enrollments = pd.read_csv(ENROLLMENTS_PATH)

def recommend_courses(user_id):


    user = users[
        users["user_id"] == user_id
    ]


    if user.empty:

        return {
            "error":"User not found"
        }



    user = user.iloc[0]


    domain = user[
        "primary_domain_interest"
    ]

    level = user[
        "current_level"
    ]



    recommended = courses[

        (courses["domain"] == domain)

        &

        (courses["level"] == level)

    ]



    # remove unavailable courses

    recommended = recommended[

        recommended["status"] == "Published"

    ]



    # recommendation score

    recommended["rating_score"] = (
        recommended["rating"] / 5
    )

    recommended["popularity_score"] = (
        recommended["enrollment_count"]
        /
        recommended["enrollment_count"].max()
    )

    recommended["recommendation_score"] = (
        recommended["rating_score"] * 0.6
        +
        recommended["popularity_score"] * 0.4
    )



    recommended = recommended.sort_values(

        by="recommendation_score",

        ascending=False

    )



    return recommended.head(5).to_dict(

        orient="records"

    )