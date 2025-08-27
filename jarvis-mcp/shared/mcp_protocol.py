from pydantic import BaseModel

class JSONRPCRequest(BaseModel):
    jsonrpc: str = "2.0"
    method: str
    params: dict
    id: int

class JSONRPCResponse(BaseModel):
    jsonrpc: str = "2.0"
    result: dict = None
    error: dict = None
    id: int

class ErrorCodes:
    INVALID_REQUEST = -32600
    METHOD_NOT_FOUND = -32601
    INVALID_PARAMS = -32602
    INTERNAL_ERROR = -32603

# Example error response
# {"jsonrpc": "2.0", "error": {"code": ErrorCodes.INVALID_REQUEST, "message": "Invalid request"}, "id": 1}
