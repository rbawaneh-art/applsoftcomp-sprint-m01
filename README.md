# M01 Sprint Project

> [!NOTE]
> You have 60 minutes to clean a catastrophic CSV into tidy format while maintaining granular Git history. Then present your approach and results to the class.
>

## The Challenge

We'll use Gapminder World Data as the dataset for this sprint project. The csv files are under ./data folder. Your tasks are organized into three branches:

### Branch Structure

You must create and work in three separate branches, merging each into `master` when complete:

**Branch 1: `data-formatting`**
1. Create the tidy version of each csv file. Save them in data/preprocessed.
2. Merge the two csv files with columns `geo`, `name`, `mortality_rate`, `gdpcapita` `year` (the `geo` column must be the first column; the order of other columns are of your choice).
3. Commit and push your work, then merge into `master`.

**Branch 2: `visualization`**
1. Create a branch from the updated `master`/`main` (after merging `data-formatting`).
2. Create a scatter plot of Mortality rate (Y-axis) vs GDP per capita (X-axis) with colors indicating the year of the data sample.
3. Save the figure in paper/figs.
4. Commit and push your work, then merge into `master`.

**Branch 3: `documentation`**
1. Create a branch from the updated `master`/`main` (after merging `visualization`).
2. Write a documentation in papers/NOTE.md explaining your data cleaning strategy, visualization choices, and key insights.
3. Commit and push your work, then merge into `master`.

**Final Step: Reproducibility**
After merging all three branches into `master`, create a `run.sh` script in the project root that executes your entire pipeline. This script should process raw data, generate all outputs, and create the final visualization. Test it by deleting your generated files and running `bash run.sh` to verify everything reproduces correctly. Commit and push this script to `master`.

Make atomic commits for each step (you can make multiple commits per step, which is encouraged).

## The Rules

- **Time:** 60 minutes of work, followed by presentations.
- **Branching:** You must create three separate branches (`data-formatting`, `visualization`, `documentation`) and complete the corresponding tasks in each branch. Merge each branch into `master` after completing the tasks.
- **Version Control:** Every change must be committed and pushed. No batch commits. Your commit messages must explain why you made each change. Each branch must have a clear commit history showing your progression through that phase of work.
- **Requirements:** Final dataset must be truly tidy. No metadata in data cells, no implicit missing values, no ambiguous column names.

## Evaluation

Judges evaluate four dimensions:

**Data Quality (25%):** Is the dataset immediately usable for analysis? Are types correct and missing values explicit?
**Git History (25%):** Do commits tell a story? Are they atomic and well-described?
**Documentation (30%):** Can you clearly explain your cleaning strategy and key decisions?
**Reproducibility (20%):** Does your run.sh script successfully recreate all results from scratch?

## Git Workflow Quick Reference

Here's the workflow you'll follow for each branch:

```bash
# Branch 1: Data Formatting
git checkout -b data-formatting
# ... do your data cleaning work, commit frequently ...
git add .
git commit -m "Your descriptive message"
git push -u origin data-formatting
git checkout master
git merge data-formatting
git push origin master

# Branch 2: Visualization
git checkout -b visualization
# ... create your plots, commit frequently ...
git add .
git commit -m "Your descriptive message"
git push -u origin visualization
git checkout master
git merge visualization
git push origin master

# Branch 3: Documentation
git checkout -b documentation
# ... write your notes, commit frequently ...
git add .
git commit -m "Your descriptive message"
git push -u origin documentation
git checkout master
git merge documentation
git push origin master

# Final: Reproducibility Script
# After all branches are merged, create run.sh
git add run.sh
git commit -m "Add reproducibility script for complete pipeline"
git push origin master
```

## Reproducibility: Dependencies and Automation

Science demands reproducibility. Your analysis might be brilliant, but if no one else can recreate your results, it loses much of its value. Reproducibility requires two critical components: locked dependencies and automated execution.

### Managing Dependencies with uv

Different Python versions and library versions can produce different results. The pandas version you use today might handle data differently than the version someone else installs tomorrow. This is why we use `uv` for dependency management in this project.

When you install packages using `uv add <package-name>`, uv automatically updates your `pyproject.toml` file with the package name and updates `uv.lock` with the exact versions of all dependencies. This lock file ensures that anyone running your code gets precisely the same library versions you used. Never manually edit `uv.lock`. Let uv manage it for you.

Before you submit, verify that your `pyproject.toml` includes all packages your scripts need. Check that your Python version is specified correctly in the `requires-python` field. When someone clones your repository and runs `uv sync`, they should get an identical environment to yours.

### The run.sh Script

Beyond locked dependencies, you need automated execution. Create a shell script named `run.sh` in the root of your project that executes your entire pipeline from start to finish. This script should use uv to ensure the correct Python environment.

Your script needs to accomplish several things. First, it should sync the environment using `uv sync` to install all dependencies from the lock file. Then it should execute your data processing scripts using `uv run python <script>` to ensure they run in the correct environment. Each step should process the raw data files in the data folder, generate the tidy datasets in data/preprocessed, and create the visualization in paper/figs.

Here's the pattern your run.sh should follow:

```bash
#!/bin/bash

# Sync dependencies from lock file
uv sync

# Run your pipeline steps
uv run python workflow/process_mortality.py
uv run python workflow/process_gdp.py
uv run python workflow/merge_data.py
uv run python workflow/create_visualization.py
```

Your actual script will use the filenames you created. The key principle remains the same: each command uses `uv run` to execute Python scripts in the locked environment.

Make sure your script is executable with `chmod +x run.sh`. Then test it thoroughly. Remove your generated files and run `bash run.sh` to verify it produces identical results. This final check ensures your work is truly reproducible. When someone clones your repository three years from now, they should be able to run this single command and recreate everything.

## Submission

Submit the link to your GitHub repository to Brightspace. We will review your commit history across all branches, and we expect to find a working run.sh script that reproduces your entire analysis pipeline.

## Set up

Start by installing [uv](https://docs.astral.sh/uv/getting-started/installation/), a modern Python package manager that ensures reproducible environments. Once installed, uv handles everything: creating virtual environments, installing packages, and locking dependencies.

The project already has a `pyproject.toml` file with essential dependencies. You should update the project name in this file to something meaningful for your work. When you need additional Python packages, install them using:

```bash
uv add <package-name>
```

This command does three things automatically. It installs the package in your project's virtual environment, adds it to `pyproject.toml`, and updates `uv.lock` with exact version information. The lock file guarantees that anyone running your code gets identical package versions.

To sync your environment with the project's dependencies (useful after cloning or when `pyproject.toml` changes), run:

```bash
uv sync
```

To run Python scripts in your project environment, use:

```bash
uv run python <script-name>.py
```

If you prefer working in Jupyter notebooks and need to install system dependencies beyond Python packages, you can use conda or mamba. Install miniforge from [GitHub - conda-forge/miniforge](https://github.com/conda-forge/miniforge), then create an environment:

```bash
mamba create -n sprint_env python=3.9
mamba activate sprint_env
mamba install -y -c conda-forge ipykernel
python -m ipykernel install --user --name sprint_kernel
```

However, for this sprint project, uv should handle all your needs. The packages in `pyproject.toml` (pandas, matplotlib, seaborn) are sufficient for the tasks ahead.

## Kickstarter code

```python
import pandas as pd

# Load the data
data_table = pd.read_csv('./data/data.csv')

# Tidy the data
# e.g., pd.melt(), pd.pivot_table(), etc. or custom code (using for loops if needed)

# Save the tidy data
# This is just a placeholder
tidy_data_table.to_csv('./data/preprocessed/tidy_data.csv', index=False)
```


```python
import matplotlib.pyplot as plt
import seaborn as sns

# Load the tidy data
tidy_mortality_data = pd.read_csv('./data/preprocessed/tidy_mortality_data.csv')
tidy_gdp_data = pd.read_csv('./data/preprocessed/tidy_gdp_data.csv')

# Merge the datasets with key column geo and year
data_table = pd.merge(tidy_mortality_data, tidy_gdp_data, on=['geo', 'year'])

# Plot the scatter plot
# Use sns.scatterplot plot with colors indicating the year of the data sample
```
