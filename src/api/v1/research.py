from fastapi import APIRouter

from src.schemas.research import ResearchRequest ,ResearchResponse

router = APIRouter()

@router.post(
        "/research",
        response_model=ResearchResponse
)
def research(request : ResearchRequest):

    return ResearchResponse(
        question = request.question,
        status = "recived"
    )