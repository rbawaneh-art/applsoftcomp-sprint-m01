#!/usr/bin/env bash
set -euo pipefail

echo "==> Installing dependencies..."
uv sync

echo "==> Running Phase 1..."
uv run python workflow/phase1_data_formatting.py

echo "==> Running Phase 2..."
uv run python workflow/phase2_visualization.py

echo "✅ Pipeline complete."
echo "Check outputs:"
echo " - data/preprocessed/"
echo " - paper/figs/"
