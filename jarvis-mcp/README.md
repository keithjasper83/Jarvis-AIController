# Jarvis MCP Suite

Production-ready, fully FOSS, Dockerized Model Control/Context Protocol suite for orchestrating three model tiers (small/medium/large), supporting LM Studio or internal Linux model runners, and maintaining a live project index robust to incremental, human-in-the-loop development.

## Features
- Three model tiers: small (scaffolder), medium (primer), large (project-wide reasoning)
- Continuous, idempotent code indexer (AST, symbols, embeddings, commit history)
- Router MCP: brokers tasks to model backends via JSON-RPC over HTTP/WebSocket
- Toggleable model runners: LM Studio, llama.cpp, or Ollama
- One-command `docker compose up` for full stack
- Healthchecks, metrics, structured logs
- Hot-reload for API services
- Pure FOSS stack, no SaaS keys required

## Quickstart
```sh
git clone <repo-url>
cd jarvis-mcp
cp .env.example .env
docker compose up --build
```

## Example Requests
See `examples/requests.http` and `examples/tasks/` for sample flows.

## Service Ports
- router: 8500
- indexer: 8600
- model-small: 8611
- model-medium: 8622
- model-large: 8633

## Model Runners
- LM Studio: set `RUNNER_MODE=lmstudio`
- llama.cpp: set `RUNNER_MODE=llama_cpp`
- Ollama: set `RUNNER_MODE=ollama`

## Volumes
- `./project` → `/workspace/project`
- `./models` → `/models`
- `./data` → `/data`

## Health Endpoints
- `/health` on all services

## License
MIT. See `NOTICE.md` for third-party tools.
