import logging

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Response,

)

from api.confluence import get_client, UpstreamProviderError
from api.helpers import settings, CustomBearer  #
from api.models import Query

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/search", dependencies=[Depends(CustomBearer())])
def search(query: Query, response: Response):
    logger.debug(f'Search request: {query}')
    client = get_client(settings)
    try:
        data = client.search(query.query)
        logger.info(f"Found {len(data)} results")
    except UpstreamProviderError as error:
        raise HTTPException(status_code=502, detail=f"{error.message}")
    response.headers["X-Connector-Id"] = "leanovate_confluence"
    return {"results": data}