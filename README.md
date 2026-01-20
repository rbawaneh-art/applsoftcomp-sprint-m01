# M01 Sprint Project

> [!NOTE]
> You have 60 minutes to clean a catastrophic CSV into tidy format while maintaining granular Git history. Then present your approach and results to the class.
>

## The Challenge

We'll use Gapminder World Data as the dataset for this sprint project. The csv files are under ./data folder. Your tasks are:

1. Create the tidy version of each csv file. Save them in data/preprocessed.
2. Merge the two csv files with columns `geo`, `name`, `mortality_rate`, `gdpcapita` `year` (the `geo` column must be the first column; the order of other columns are of your choice). 
3. Create a scatter plot of Mortality rate (Y-axis) vs GDP per capita (X-axis) with colors indicating the year of the data sample.
4. Save the figure in paper/figs and write a documentation in papers/NOTE.md.

Make atomic commits for each step (you can make multiple commits per step, which is encouraged).


## The Rules

- **Time:** 60 minutes of work, followed by presentations.
- **Version Control:** Every change must be committed and pushed. No batch commits. Your commit messages must explain why you made each change.
- **Requirements:** Final dataset must be truly tidy. No metadata in data cells, no implicit missing values, no ambiguous column names.

## Evaluation

Judges evaluate three dimensions:

**Data Quality (30%):** Is the dataset immediately usable for analysis? Are types correct and missing values explicit?
**Git History (30%):** Do commits tell a story? Are they atomic and well-described?
**Documentation (40%):** Can you clearly explain your cleaning strategy and key decisions?

## Submission

Submit the link to your GitHub repository to Brightspace. 

## Set up

Install [uv](https://docs.astral.sh/uv/getting-started/installation/). And then create a virtual environment using:

Open `pyproject.toml` in a text editor and change the project name and add your project dependencies.

If you want to install a Python package, run:

```bash 
uv add <package-name>
```

If you need to install non-Python dependencies, you can use conda or mamba as described below.

#### Miniforge

Install miniforge [GitHub - conda-forge/miniforge: A conda-forge distribution.](https://github.com/conda-forge/miniforge).

First create a virtual environment for the project.

    mamba create -n project_env_name python=3.7
    mamba activate project_env_name

Install `ipykernel` for Jupyter. 

    mamba install -y -c bioconda -c conda-forge ipykernel numpy pandas scipy matplotlib seaborn tqdm

Create a kernel for the virtual environment that you can use in Jupyter lab/notebook.

    python -m ipykernel install --user --name project_env_kernel_name
