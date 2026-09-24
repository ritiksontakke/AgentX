from fastapi import FastAPI

from src.api.v1.research import router

app = FastAPI(
    title="AI Research Agent"
)

@app.get("/helath")
def health_check():
    return{
        "status" : "ok"
    }

app.include_router(
    router
)