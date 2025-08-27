#!/bin/zsh
# Run smoke tests before tagging
./jarvis-mcp/smoke_test.sh || exit 1

# Tag the commit as working if tests pass
tag_name="working-$(date +%Y%m%d%H%M%S)"
git tag "$tag_name"
git push origin --tags

echo "Tagged and pushed as $tag_name"
