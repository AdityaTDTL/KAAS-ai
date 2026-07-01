from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.api.routes import router

app = FastAPI(title="AI Service")

app.include_router(router)

@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")
