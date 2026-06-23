import os
from groq import Groq
from app.config.settings import GROQ_API_KEY

client = Groq(
    api_key=GROQ_API_KEY
)

def generate_explanation(
        user_profile,
        history,
        courses
):

    prompt = f"""

You are an AI learning assistant for KaaS platform.

Learner Profile:

{user_profile}


Learning History:

{history}


Recommended Courses:

{courses}


Explain:

1. Why these courses are recommended
2. How they match learner goals
3. Give personalized advice

Keep answer simple and helpful.

"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
