from pydantic import BaseModel

class MCPRequest(BaseModel):
    task: str
    tier: str = None
    needs_index: bool = False
    manifest: list = None

class MCPResponse(BaseModel):
    result: dict
