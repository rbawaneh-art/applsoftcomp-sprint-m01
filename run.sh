#!/usr/bin/env bash
set -euo pipefail

echo "==> Syncing dependencies using uv..."
uv sync

echo "==> Running full pipeline (data formatting + visualization)..."
uv run python workflow/Merged_plot_code.py

echo "✅ Pipeline finished successfully."
echo "Generated outputs:"
echo " - data/preprocessed/merged_mortality_gdp.csv"
echo " - paper/figs/mortality_vs_gdp_scatter.png"
