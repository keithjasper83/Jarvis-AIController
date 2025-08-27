from fastapi.testclient import TestClient
from server import app

client = TestClient(app)

def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"

def test_mcp_scaffold():
    resp = client.post("/mcp.scaffold", json={"task": "scaffold something"})
    assert resp.status_code == 200
    assert "Small model handled" in resp.json()["result"]
