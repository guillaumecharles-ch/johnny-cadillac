#!/usr/bin/env bash
# Ajoute au classement commun un code JC1- reçu par message, puis publie.
#   ./ajouter-score.sh JC1-eyJuIjoi...
set -euo pipefail
cd "$(dirname "$0")"

if [ $# -eq 0 ]; then
  echo "Usage : ./ajouter-score.sh JC1-…" >&2
  exit 1
fi

python3 .github/scripts/ajouter_score.py "$@"

if git diff --quiet -- scores.json; then
  echo "Classement inchangé, rien à publier."
  exit 0
fi

git add scores.json
git commit -q -m "Classement : ajout d'un score reçu par message"
git push -q
echo "Publié. Le classement est à jour dans la minute."
