# M01 Sprint: Data Cleaning & Reproducibility

**Time Limit:** 60 minutes of work, followed by class presentations

## Overview

This sprint challenges you to clean messy Gapminder World Data into tidy format while maintaining granular Git history. You'll work through three distinct phases (each in its own Git branch), then create a reproducibility script that allows anyone to recreate your entire pipeline.

## Instructions

Work through four phases, creating a separate Git branch for the first three:

**Phase 1: data-formatting**

Transform the messy CSV files in your data folder into tidy format. What does tidy mean? One variable per column, one observation per row, no metadata hiding in data cells, explicit missing values, and clear column names. Save your cleaned files to `data/preprocessed`. Then merge the two datasets into a single table with columns `geo`, `name`, `mortality_rate`, `gdpcapita`, and `year` (geo must be the first column). Commit your work frequently with clear messages explaining your reasoning, push to GitHub, and merge into master.

**Phase 2: visualization**

Create a new branch from your updated master. Build a scatter plot showing child mortality rate (Y-axis) versus GDP per capita (X-axis), with colors indicating the year of each observation. Save your figure to `paper/figs`. Commit your visualization code and output, push to GitHub, and merge into master.

**Phase 3: documentation**

Branch again from updated master. Write a document at `paper/NOTE.md` that explains your data cleaning strategy, visualization choices, and the key insights revealed by your analysis. This documentation should help future collaborators understand not just what you did, but why you made those choices. Commit, push to GitHub, and merge into master.

**Phase 4: reproducibility**

After merging all three branches, create a shell script called `run.sh` in your project root. This script must execute your entire pipeline from raw data to final figure. Use `uv sync` to install dependencies and `uv run python <script>` to execute your workflow scripts. Test your script by deleting all generated files and running `bash run.sh` to verify it recreates everything. Commit this script to master.

## Git Workflow

For each of the first three phases, follow this pattern:

```bash
git checkout -b branch-name
# work and commit frequently with clear messages
git push -u origin branch-name
git checkout master
git merge branch-name
git push origin master
```

Your commit history tells a story. Make each commit atomic (one logical change) and write messages that explain your reasoning, not just what changed.

## Reproducibility Script Structure

Your `run.sh` should follow this general pattern:

```bash
#!/bin/bash
uv sync
uv run python workflow/process_mortality.py
uv run python workflow/process_gdp.py
uv run python workflow/merge_data.py
uv run python workflow/create_visualization.py
```

Use `chmod +x run.sh` to make it executable. The script should use `uv sync` to ensure identical package versions (via `uv.lock`) and `uv run` to execute scripts in the correct environment.

## Evaluation Criteria

Your work will be evaluated across four dimensions:

- **Data Quality (20%):** Is your dataset immediately usable for analysis? Are data types correct and missing values explicit?
- **Git History (20%):** Do your commits tell a coherent story with clear reasoning?
- **Documentation (30%):** Can you clearly explain your cleaning strategy, visualization choices, and insights?
- **Reproducibility (30%):** Does your `run.sh` script successfully recreate all results from scratch?

## Setup

Before you begin, install uv for dependency management:

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install additional packages if needed
uv add <package-name>

# Run your scripts
uv run python <script>.py
```

The project already includes pandas, matplotlib, and seaborn in `pyproject.toml`, which should be sufficient for this sprint.

## Submission

Submit the link to your GitHub repository on Brightspace. We will review your commit history across all branches and verify that your `run.sh` script successfully reproduces your analysis.
