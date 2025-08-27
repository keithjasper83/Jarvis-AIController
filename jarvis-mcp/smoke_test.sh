#!/bin/bash
set -e
SERVICES=(model-small model-medium model-large router indexer)
for svc in "${SERVICES[@]}"; do
  echo "Testing $svc:"
  docker compose exec $svc pytest || { echo "$svc tests failed"; exit 1; }
done
echo "All tests passed."
