from .policies import select_backend
from .clients.lmstudio_client import LMStudioClient
from .clients.llama_cpp_client import LlamaCppClient
from .clients.ollama_client import OllamaClient
from .schemas import MCPRequest, MCPResponse
from .settings import settings

class MCPRouter:
    def __init__(self):
        self.clients = {
            "lmstudio": LMStudioClient(settings.LMSTUDIO_BASE_URL),
            "llama_cpp": LlamaCppClient(),
            "ollama": OllamaClient()
        }
    async def handle(self, method, payload):
        req = MCPRequest(**payload)
        backend = select_backend(method, req, settings)
        client = self.clients[settings.RUNNER_MODE]
        # Proxy to backend or client
        result = await client.call_method(method, req)
        return MCPResponse(result=result).dict()
