#!/usr/bin/env bash
set -e
REMOTE_URL=${1:-}
cd "$(dirname "$0")"
if [ ! -d .git ]; then
  git init
fi

git add .
if git commit -m "Deploy: update site"; then
  :
else
  echo "No changes to commit"
fi

if [ -n "$REMOTE_URL" ]; then
  git remote remove origin 2>/dev/null || true
  git remote add origin "$REMOTE_URL"
  git branch -M main
  git push -u origin main
else
  echo "No remote URL provided. Usage: ./deploy.sh <git-remote-url>"
fi
