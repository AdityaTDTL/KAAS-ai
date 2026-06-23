from groq import Groq
from app.config.settings import GROQ_API_KEY


client = Groq(
    api_key=GROQ_API_KEY
)


def ask_llm(question, learner_context=None):

    system_prompt = "You are KaaS AI Tutor. Explain concepts clearly."
    if learner_context:
        system_prompt += f"\nHere is the context about the learner asking the question: {learner_context}"

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",

        messages=[

            {
                "role": "system",
                "content": system_prompt
            },

            {
                "role": "user",
                "content": question
            }
        ]   
    )


    return response.choices[0].message.content

