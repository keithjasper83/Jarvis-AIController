from fastapi import FastAPI
from .api import router

app = FastAPI(title="Jarvis MCP Indexer")
app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok"}
