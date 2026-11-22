#!/usr/bin/env bash
# Exo Git (slide 26) : rejoue les parties 1 a 8 et 11 en local.
# Cree ./my-first-repo et ./bash-installer avec un vrai historique git.
# Usage : bash git_workflow.sh
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
INSTALL="$HERE/../01-bash/install.sh"
cd "$HERE"
rm -rf my-first-repo bash-installer

# ---- Parties 1 a 8 : my-first-repo
git --version
mkdir my-first-repo && cd my-first-repo
git init -b main
touch readme.txt
git status
git add readme.txt
git commit -m "Add readme file"
git log

echo "Hello Git" >> readme.txt
git status
git add readme.txt
git commit -m "Update readme with first line"
git log --oneline
git diff HEAD~1

git branch
git branch feature-script
git switch feature-script
git switch -c dev
git switch feature-script
git branch --show-current

cat > install.sh <<'EOF'
#!/bin/bash
echo "Starting installation..."
sudo apt-get update
sudo apt-get install -y git
echo "Installation complete!"
EOF
chmod +x install.sh
git add install.sh
git commit -m "Add install script"
git log --oneline --graph --all

git switch main
ls   # install.sh absent : il n'existe que sur feature-script
git merge feature-script
ls   # install.sh est maintenant la
git log --oneline
git branch -d feature-script
cd ..

# ---- Partie 11 : bash-installer
mkdir bash-installer && cd bash-installer
git init -b main
cat > README.md <<'EOF'
# bash-installer
Petit projet qui contient un script d'installation d'environnement de dev.
EOF
git add README.md
git commit -m "Add README"
git switch -c feature-install
cp "$INSTALL" install.sh
chmod +x install.sh
git add install.sh
git commit -m "Add installation script"
git switch main
git merge feature-install
git branch -d feature-install
git log --oneline
