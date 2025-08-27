from fastapi import APIRouter, Request
from .index_pipeline import reindex, search_index, pull_context, get_stats

router = APIRouter()

@router.post("/reindex")
async def reindex_endpoint(req: Request):
    payload = await req.json()
    return reindex(payload)

@router.post("/search_index")
async def search_index_endpoint(req: Request):
    payload = await req.json()
    return search_index(payload)

@router.post("/pull_context")
async def pull_context_endpoint(req: Request):
    payload = await req.json()
    return pull_context(payload)

@router.get("/stats")
def stats_endpoint():
    return get_stats()
