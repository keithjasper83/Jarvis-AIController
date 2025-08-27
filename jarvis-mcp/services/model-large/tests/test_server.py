from fastapi.testclient import TestClient
from server import app

client = TestClient(app)

def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"

def test_mcp_refactor():
    resp = client.post("/mcp.refactor", json={"task": "refactor something"})
    assert resp.status_code == 200
    assert "Large model handled" in resp.json()["result"]
