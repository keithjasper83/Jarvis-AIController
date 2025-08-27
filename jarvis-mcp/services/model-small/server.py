from fastapi import FastAPI, Request
import os

app = FastAPI(title="Jarvis MCP Model Small")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/mcp.{method}")
async def mcp_method(method: str, req: Request):
    payload = await req.json()
    # Simulate small-tier logic
    return {"result": f"Small model handled {method} for {payload.get('task', '')}"}
