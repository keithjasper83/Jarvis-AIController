import httpx

class LlamaCppClient:
    def __init__(self, base_url=None):
        self.base_url = base_url or "http://localhost:8080"
    async def call_method(self, method, req):
        async with httpx.AsyncClient() as client:
            resp = await client.post(f"{self.base_url}/v1/chat/completions", json={
                "messages": [{"role": "user", "content": req.task}],
                "model": "llama-small",
                "max_tokens": 1024
            })
            return resp.json()
