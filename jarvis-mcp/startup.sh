#!/bin/bash
set -e
echo "Building and starting all MCP suite services..."
docker compose up --build
