# M01 Sprint Project

::: {.callout-note title="The Sprint Challenge"}
You have 60 minutes to transform messy CSV data into tidy format while maintaining granular Git history. Then you'll present your approach and results to the class.
:::

## What You're Building

Let's talk about real-world data work. The Gapminder World Data sitting in your data folder looks deceptively simple, but it harbors the kinds of problems you'll encounter throughout your career: metadata mixed with data, implicit missing values, years spread across columns instead of properly structured rows. Your task is to clean this data properly, visualize the relationship between child mortality and GDP, and document your decisions along the way.

This sprint teaches you something crucial about computational science. The work itself matters, but so does how you organize and communicate that work. You'll move through three distinct phases, each in its own Git branch, building toward a complete and reproducible analysis pipeline.

## The Journey Through Three Phases

Your work unfolds in three stages, each with its own branch. Think of these branches as parallel universes where you can experiment freely before integrating your work into the main timeline.

**Start with data formatting.** Create a branch called `data-formatting` and begin the real work. The CSV files in your data folder need to become truly tidy. What does tidy mean? Each variable forms a column. Each observation forms a row. Each type of observational unit forms a table. No metadata hiding in data cells. No missing values represented by blank spaces or dashes. No ambiguous column names that leave future readers guessing.

Transform each CSV file into its tidy version and save these in data/preprocessed. Then merge your two cleaned datasets into a single table with columns `geo`, `name`, `mortality_rate`, `gdpcapita`, and `year`. The `geo` column must come first. The order of other columns is your choice, but make that choice deliberately. When this phase is complete, commit your changes with messages that explain why you made each decision, push to GitHub, and merge back into master.

**Move to visualization.** Create a new branch called `visualization` from your updated master. Now you have clean data to work with, and patterns wait to be discovered. Create a scatter plot showing child mortality rate on the Y-axis and GDP per capita on the X-axis. Use color to indicate the year of each data point. This visual should reveal how the relationship between wealth and child survival has evolved over time.

Save your figure in paper/figs. Pay attention to your visualization choices. Are your axes scaled appropriately? Do your colors convey meaning clearly? Can someone unfamiliar with your data understand what they're seeing? Commit your visualization code and output, push to GitHub, and merge into master.

**Complete with documentation.** Branch again, this time calling it `documentation`. Write a document at paper/NOTE.md that explains your journey. Walk your reader through your data cleaning strategy. Why did you make the choices you made? What problems did you encounter in the raw data, and how did you resolve them? Discuss your visualization decisions. What patterns emerge from your plot? What story does the data tell about global development?

This documentation matters as much as your code. Future collaborators, including your future self, need to understand not just what you did, but why you did it. Make your reasoning transparent. Commit your documentation, push to GitHub, and merge into master.

**Ensure reproducibility.** After merging all three branches, your final task requires a different kind of work. Create a shell script called `run.sh` in your project root. This script should execute your entire pipeline from raw data to final figure. Someone should be able to clone your repository, run `bash run.sh`, and reproduce everything you created. This automation ensures your work can be verified, extended, and built upon.

## How Git Structures Your Work

Understanding the branching workflow is essential. When you create a branch with `git checkout -b data-formatting`, you're creating a safe space to experiment. Work in that branch, making frequent commits as you progress. Each commit should represent a logical unit of work. When you add a file with `git add .`, write a commit message with `git commit -m "Your descriptive message"` that explains the why behind your change, not just the what.

Push your branch to GitHub with `git push -u origin data-formatting` so your work is backed up and visible. When your work in that branch is complete, switch back to master with `git checkout master`, merge your branch with `git merge data-formatting`, and push the updated master to GitHub with `git push origin master`. Then repeat this cycle for visualization and documentation.

Your commit history tells a story. Make that story clear. Avoid batch commits that bundle unrelated changes. Each commit should advance your work by one logical step. Your commit messages should explain your reasoning. Future readers, whether colleagues or graders, will follow your thought process through these commits.

After merging all three branches, add your `run.sh` script directly to master with `git add run.sh`, commit it with a clear message about ensuring reproducibility, and push to GitHub. This final commit caps your project with the automation that makes everything reproducible.

## What Distinguishes Excellent Work

Your work will be evaluated across four dimensions, each revealing different aspects of computational competence.

Data quality accounts for 25% of your evaluation. Can someone immediately use your dataset for analysis without further cleaning? Are data types correct and missing values explicitly marked? Does your merged dataset follow tidy data principles? The test is simple: if another analyst loads your preprocessed data, can they start analyzing immediately?

Git history makes up another 25%. Do your commits tell a coherent story of your work? Are they atomic, each representing one logical change? Do your commit messages explain your reasoning? Can someone understand your decision-making process by reading your commit history? Your Git timeline should document not just what you did, but why.

Documentation carries 30% of the weight. Can you clearly articulate your cleaning strategy? Do you explain why you made specific choices? Does your visualization discussion reveal insights from the data? Good documentation doesn't just describe what happened. It explains the reasoning behind decisions and interprets what the results mean.

Reproducibility comprises the final 20%. Does your `run.sh` script successfully recreate all results from scratch? Can someone clone your repository and reproduce your work without manual intervention? Does your `uv.lock` file ensure consistent package versions? Reproducibility is the foundation of scientific computing. Without it, your results cannot be verified or built upon.

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

## Getting Started

Start by installing [uv](https://docs.astral.sh/uv/getting-started/installation/), a modern Python package manager that ensures reproducible environments. Once installed, uv handles everything: creating virtual environments, installing packages, and locking dependencies.

The project already has a `pyproject.toml` file with essential dependencies. You should update the project name in this file to something meaningful for your work. When you need additional Python packages, install them using `uv add <package-name>`. This command does three things automatically: it installs the package in your project's virtual environment, adds it to `pyproject.toml`, and updates `uv.lock` with exact version information. The lock file guarantees that anyone running your code gets identical package versions.

To sync your environment with the project's dependencies (useful after cloning or when `pyproject.toml` changes), run `uv sync`. To run Python scripts in your project environment, use `uv run python <script-name>.py`.

If you prefer working in Jupyter notebooks and need to install system dependencies beyond Python packages, you can use conda or mamba. Install miniforge from [GitHub - conda-forge/miniforge](https://github.com/conda-forge/miniforge), then create an environment with `mamba create -n sprint_env python=3.9`, activate it with `mamba activate sprint_env`, install ipykernel with `mamba install -y -c conda-forge ipykernel`, and create a kernel with `python -m ipykernel install --user --name sprint_kernel`.

However, for this sprint project, uv should handle all your needs. The packages in `pyproject.toml` (pandas, matplotlib, seaborn) are sufficient for the tasks ahead.

## Code to Get You Started

Here's some kickstarter code to guide your initial work:

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

For visualization:

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Load the tidy data
tidy_mortality_data = pd.read_csv('./data/preprocessed/tidy_mortality_data.csv')
tidy_gdp_data = pd.read_csv('./data/preprocessed/tidy_gdp_data.csv')

# Merge the datasets with key column geo and year
data_table = pd.merge(tidy_mortality_data, tidy_gdp_data, on=['geo', 'year'])

# Plot the scatter plot
# Use sns.scatterplot with colors indicating the year of the data sample
```

## Submission

Submit the link to your GitHub repository to Brightspace. We will review your commit history across all branches, and we expect to find a working run.sh script that reproduces your entire analysis pipeline. You have 60 minutes for the work itself, followed by class presentations where you'll explain your approach and findings.
