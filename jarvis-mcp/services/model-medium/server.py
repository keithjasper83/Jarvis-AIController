from fastapi import FastAPI, Request
import os

app = FastAPI(title="Jarvis MCP Model Medium")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/mcp.{method}")
async def mcp_method(method: str, req: Request):
    payload = await req.json()
    # Simulate medium-tier logic
    return {"result": f"Medium model handled {method} for {payload.get('task', '')}"}
