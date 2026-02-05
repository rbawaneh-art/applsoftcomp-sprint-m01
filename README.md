# M01 Sprint Project

>[!NOTE]
> You have 60 minutes to clean catastrophic CSV data into tidy format while maintaining granular Git history. Then present your approach and results.
>

This sprint challenges you to clean messy Data into tidy format while maintaining granular Git history. **Time Limit:** 60 minutes of work, followed by class presentations. 

Repo: https://github.com/skojaku/applsoftcomp-sprint-m01

Clone the repo under your local by 

```bash
git clone <url>
```
where url is `https://github.com/skojaku/applsoftcomp-sprint-m01`.

### Instructions
**Phase 1: data-formatting**: Create a new branch from your master/main. Transform the messy CSV files in your data folder into tidy format. Save your cleaned files to `data/preprocessed`. Then merge the two datasets into a single table with columns `geo`, `name`, `mortality_rate`, `gdpcapita`, and `year` (geo must be the first column). Commit your work frequently with clear messages explaining your reasoning, and merge into master.

**Phase 2: visualization**: Create a new branch from your updated master. Build a scatter plot showing child mortality rate (Y-axis) versus GDP per capita (X-axis), with colors indicating the year of each observation. Save your figure to `paper/figs`. Commit your visualization code and output, push to GitHub, and merge into master.

**Phase 3: documentation**: Branch again from updated master/main. Write a document at `paper/NOTE.md` that explains your data cleaning strategy, visualization choices, and the key insights revealed by your analysis. This documentation should help future collaborators understand not just what you did, but why you made those choices. Commit, push to GitHub, and merge into master.

**Phase 4: reproducibility**: After merging all three branches, create a shell script called `run.sh` in your project root. This script must execute your entire pipeline from raw data to final figure. Use `uv sync` to install dependencies and `uv run python <script>` to execute your workflow scripts. Test your script by deleting all generated files and running `bash run.sh` to verify it recreates everything. Commit this script to master.

Submit the link to your GitHub repository on Brightspace. We will review your commit history across all branches and verify that your `run.sh` script successfully reproduces your analysis.
#### Evaluation Criteria

- **Data Quality (20%):** Is your dataset immediately usable for analysis? Are data types correct and missing values explicit?
- **Git History (20%):** Do your commits tell a coherent story with clear reasoning?
- **Documentation (30%):** Can you clearly explain your cleaning strategy, visualization choices, and insights?
- **Reproducibility (30%):** Does your `run.sh` script successfully recreate all results from scratch?



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

## Reproducibility Requirements

Your `run.sh` script structur some like this (not necessarily the exact structure but just a general idea):

```bash
#!/bin/bash
uv sync
uv run python workflow/process_mortality.py
uv run python workflow/process_gdp.py
uv run python workflow/merge_data.py
uv run python workflow/create_visualization.py
```

**Dependency Management:**
- Install packages: `uv add <package-name>`
- This updates `pyproject.toml` and creates `uv.lock` with exact versions
- Never edit `uv.lock` manually
- When someone clones your repo and runs `uv sync`, they get identical package versions
- Make script executable: `chmod +x run.sh`

## Setup

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/)
2. Update project name in `pyproject.toml`
3. Install packages: `uv add <package-name>`
4. Run scripts: `uv run python <script>.py`

The existing dependencies (pandas, matplotlib, seaborn) are sufficient for this project.

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
