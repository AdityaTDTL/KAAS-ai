import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
ENROLLMENT_PATH = os.path.join(BASE_DIR, "data", "datasets", "enrollments.csv")

enrollments = pd.read_csv(ENROLLMENT_PATH)

def get_learning_history(user_id):
    user_courses = enrollments[
        enrollments["user_id"] == user_id
    ]

    if user_courses.empty:
        return {
            "completed_courses": [],
            "in_progress_courses": [],
            "average_score":0
        }

    completed = user_courses[
        user_courses["completion_status"] == "Completed"
    ]

    in_progress = user_courses[
        user_courses["completion_status"] != "Completed"
    ]

    avg_score = user_courses["final_score"].mean()

    return {
        "completed_courses": completed["course_id"].tolist(),
        "in_progress_courses": in_progress["course_id"].tolist(),
        "average_score": round(avg_score,2)
    }
