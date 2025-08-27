from fastapi import FastAPI, Request
from .mcp_router import MCPRouter
from .settings import settings

app = FastAPI(title="Jarvis MCP Router")
router = MCPRouter()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/mcp.{method}")
async def mcp_method(method: str, req: Request):
    payload = await req.json()
    return await router.handle(method, payload)
