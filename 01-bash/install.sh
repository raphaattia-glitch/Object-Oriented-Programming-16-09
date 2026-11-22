#!/usr/bin/env bash
# Exo Bash (slide 18) : configurer un environnement de dev from scratch.
# Usage : bash install.sh
set -euo pipefail

echo "Starting installation..."

OS="$(uname -s)"

install_pkg() {
  local pkg="$1"
  if command -v "$pkg" >/dev/null 2>&1; then
    echo "[ok] $pkg est deja installe"
    return
  fi
  echo "[..] installation de $pkg"
  case "$OS" in
    Darwin) brew install "$pkg" ;;
    Linux)  sudo apt-get install -y "$pkg" ;;
    *)      echo "OS non supporte : $OS"; exit 1 ;;
  esac
}

# 1. Mise a jour des listes de paquets
case "$OS" in
  Darwin) command -v brew >/dev/null 2>&1 || { echo "Installe Homebrew d'abord"; exit 1; }
          brew update ;;
  Linux)  sudo apt-get update ;;
esac

# 2. Outils de base
for p in git curl python3 tree; do
  install_pkg "$p"
done

# 3. Environnement Python isole
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
  echo "[ok] venv cree dans .venv"
fi
# shellcheck disable=SC1091
source .venv/bin/activate
pip install --upgrade pip pytest

# 4. Verification
echo "--- Versions ---"
git --version
python3 --version
pytest --version

echo "Installation complete!"
