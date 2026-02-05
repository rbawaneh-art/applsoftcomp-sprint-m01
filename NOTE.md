# M01 Sprint: Data Cleaning & Reproducibility

**Time:** 60 minutes + presentations

## Your Mission

Clean messy Gapminder CSV data into tidy format. Visualize mortality vs GDP. Document your process. Make it reproducible.

## Three Phases (Three Git Branches)

### 1. data-formatting
- Tidy each CSV (one variable per column, one observation per row, explicit missing values)
- Save to `data/preprocessed`
- Merge into single table: `geo`, `name`, `mortality_rate`, `gdpcapita`, `year`
- Commit frequently, merge to master

### 2. visualization
- Scatter plot: mortality (Y) vs GDP (X), colored by year
- Save to `paper/figs`
- Commit, merge to master

### 3. documentation
- Write `paper/NOTE.md` explaining cleaning strategy, viz choices, insights
- Commit, merge to master

### 4. reproducibility
- Create `run.sh` that executes entire pipeline
- Must use: `uv sync` and `uv run python <script>`
- Test it works from scratch
- Commit to master

## Git Workflow Pattern

```bash
git checkout -b branch-name
# work and commit frequently
git push -u origin branch-name
git checkout master
git merge branch-name
git push origin master
```

## Evaluation

- **Data Quality (20%):** Tidy data, correct types, explicit missing values
- **Git History (20%):** Atomic commits with clear reasoning
- **Documentation (30%):** Clear explanations of decisions and insights
- **Reproducibility (30%):** Working `run.sh` script

## Key Requirements

✓ Three separate branches for three phases
✓ Atomic commits with meaningful messages
✓ `run.sh` script that reproduces everything
✓ `uv.lock` for exact dependency versions
✓ Clean, usable tidy data

## Setup

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install packages
uv add <package-name>

# Run scripts
uv run python <script>.py
```

## Submission

Submit GitHub repository link to Brightspace.
