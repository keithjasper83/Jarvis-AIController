#!/bin/zsh
set -e

# Local Python syntax check (no Docker required)
find "$(dirname "$0")/services" -name "*.py" -exec python3 -m py_compile {} \; || { echo "Python syntax check failed"; exit 1; }

# Optionally run pytest if available
if command -v pytest &> /dev/null; then
    pytest "$(dirname "$0")/services" || { echo "Pytest failed"; exit 1; }
fi

echo "Local tests passed (no Docker required)"

