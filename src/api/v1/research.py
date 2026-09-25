from fastapi import APIRouter,Depends

from src.schemas.research import ResearchRequest ,ResearchResponse
from src.services.research import ResearchService
from src.dependencies import get_research_service
router = APIRouter()

research_service = ResearchService
@router.post(
        "/research",
        response_model=ResearchResponse
)
def research(
    request : ResearchRequest,
    service: ResearchService = Depends(get_research_service),
):

    return service.research(request)