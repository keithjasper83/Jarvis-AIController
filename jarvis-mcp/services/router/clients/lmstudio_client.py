import httpx
import os

class LMStudioClient:
    def __init__(self, base_url):
        self.base_url = base_url
    async def call_method(self, method, req):
        # Wrap LM Studio Chat Completions API
        async with httpx.AsyncClient() as client:
            resp = await client.post(f"{self.base_url}/v1/chat/completions", json={
                "messages": [{"role": "user", "content": req.task}],
                "model": os.getenv('SMALL_MODEL'),
                "max_tokens": 1024
            })
            return resp.json()
