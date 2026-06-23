from fastapi import APIRouter

from app.llm.client import ask_llm
from app.learner_intelligence.profile_analyzer import analyze_learner
from app.api.schemas import ChatRequest
from app.recommendation.personalized_ai_recommendation import ai_recommendation

router = APIRouter(
    prefix="/api"
)

@router.get("/health")
def health_check():
    return {
        "status": "AI service healthy"
    }

@router.post("/chat")
def chat(question: str):
    answer = ask_llm(question)
    
    return {
        "question": question,
        "answer": answer
    }

@router.get("/learner/{user_id}")
def learner_profile(user_id: str):
    profile = analyze_learner(user_id)
    return profile

@router.post("/personalized-chat")
def personalized_chat(request: ChatRequest):
    learner_profile = analyze_learner(request.user_id)
    
    if "error" in learner_profile:
        return learner_profile

    answer = ask_llm(request.question, learner_profile)
    
    return {
        "user_id": request.user_id,
        "learner_profile": learner_profile,
        "answer": answer
    }


@router.get("/recommendations/{user_id}")
def recommendation(user_id:str):

    result = ai_recommendation(
        user_id
    )

    return result