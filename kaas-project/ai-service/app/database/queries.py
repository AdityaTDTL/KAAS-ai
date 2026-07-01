from app.database.connection import load_dataset



def get_user_profile(user_id):

    users = load_dataset("users.csv")


    users["user_id"] = (
        users["user_id"]
        .astype(str)
        .str.strip()
    )


    user_id = str(user_id).strip()


    user = users[
        users["user_id"] == user_id
    ]


    return user.to_dict(
        orient="records"
    )