# M01 Sprint Project

::: {.callout-note title="The Sprint Challenge"}
You have 60 minutes to clean catastrophic CSV data into tidy format while maintaining granular Git history. Then present your approach and results.
:::

## The Challenge

Transform the Gapminder World Data in your data folder into tidy format. The data has metadata mixed with observations, implicit missing values, and years spread across columns. Clean it, visualize the mortality-GDP relationship, document your decisions, and make it reproducible.

Work through three phases, each in its own Git branch. Commit frequently with clear messages explaining your reasoning. After merging all branches, create a `run.sh` script that reproduces your entire pipeline.

## Three Phases

**Phase 1: data-formatting**

Create a branch called `data-formatting`. Transform each CSV into tidy format: one variable per column, one observation per row, no metadata in data cells, explicit missing values, clear column names. Save tidy files to data/preprocessed.

Merge the two datasets into one table with columns `geo`, `name`, `mortality_rate`, `gdpcapita`, `year` (geo first). Commit, push, and merge into master.

**Phase 2: visualization**

Branch from updated master as `visualization`. Create a scatter plot with mortality rate (Y-axis) vs GDP per capita (X-axis), colored by year. Save to paper/figs. Commit, push, and merge into master.

**Phase 3: documentation**

Branch from updated master as `documentation`. Write paper/NOTE.md explaining your data cleaning strategy, visualization choices, and insights. Commit, push, and merge into master.

**Final: reproducibility**

Create `run.sh` in project root. This script must reproduce your entire pipeline from raw data to final figure. Use `uv sync` to install dependencies and `uv run python <script>` to execute your workflow scripts. Test by deleting generated files and running `bash run.sh`. Commit to master.

## Git Workflow

```bash
# For each phase
git checkout -b branch-name
# ... work and commit frequently ...
git push -u origin branch-name
git checkout master
git merge branch-name
git push origin master
```

## Evaluation

- **Data Quality (25%):** Immediately usable tidy data with correct types and explicit missing values
- **Git History (25%):** Atomic commits with clear messages explaining your reasoning
- **Documentation (30%):** Clear explanation of cleaning strategy, choices, and insights
- **Reproducibility (20%):** Working `run.sh` script that recreates all results from scratch

## Reproducibility Requirements

Your `run.sh` script ensures anyone can reproduce your work:

```bash
#!/bin/bash
uv sync
uv run python workflow/process_mortality.py
uv run python workflow/process_gdp.py
uv run python workflow/merge_data.py
uv run python workflow/create_visualization.py
```

Use `uv add <package-name>` to install packages. This updates `pyproject.toml` and creates `uv.lock` with exact versions. Never edit `uv.lock` manually. When someone clones your repo and runs `uv sync`, they get identical package versions.

Make your script executable with `chmod +x run.sh`.

## Setup

Install [uv](https://docs.astral.sh/uv/getting-started/installation/). Update the project name in `pyproject.toml`. Install packages with `uv add <package-name>`. Run scripts with `uv run python <script>.py`.

The existing dependencies (pandas, matplotlib, seaborn) are sufficient.

## Kickstarter Code

```python
import pandas as pd

# Load and tidy
data_table = pd.read_csv('./data/data.csv')
# Use pd.melt(), pd.pivot_table(), or custom code
tidy_data_table.to_csv('./data/preprocessed/tidy_data.csv', index=False)
```

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Merge and visualize
tidy_mortality = pd.read_csv('./data/preprocessed/tidy_mortality_data.csv')
tidy_gdp = pd.read_csv('./data/preprocessed/tidy_gdp_data.csv')
data_table = pd.merge(tidy_mortality, tidy_gdp, on=['geo', 'year'])
# Use sns.scatterplot with colors indicating year
```

## Submission

Submit your GitHub repository link to Brightspace. We'll review commit history across all branches and verify your `run.sh` script works.
