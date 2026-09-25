from src.schemas.research import ResearchRequest, ResearchResponse

class ResearchService:

    def research(
            self,
            request : ResearchRequest,
            
    ) -> ResearchResponse:


        return ResearchResponse(
            question=request.question,
            status="recivied"
        )