#!/bin/zsh

# Create and push new tag
TAG_NAME="working-$(date +%Y%m%d%H%M%S)"
git tag "$TAG_NAME"
git push origin --tags

echo "Created and pushed tag: $TAG_NAME"

# Cleanup: keep only the 5 most recent tags
tags_to_delete=$(git tag --sort=-creatordate | tail -n +6)
for tag in $tags_to_delete; do
    git tag -d "$tag"
    git push origin :refs/tags/$tag
    echo "Deleted old tag: $tag"
done

echo "Tag cleanup complete."
