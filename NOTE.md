# Sprint Project – Documentation (Phase 3)

## 1. Overview

This project analyzes the relationship between child mortality rate and GDP per capita over time. 
The objective is to understand how economic development relates to public health outcomes across countries.

The workflow consisted of three main phases:
1. Data formatting and cleaning
2. Visualization
3. Documentation

This document explains the reasoning behind the data preparation steps, visualization decisions, and the key insights obtained from the analysis.

---

## 2. Data Cleaning Strategy

### 2.1 Converting Wide Data to Tidy Format

Both datasets (GDP per capita and child mortality) were originally in wide format, where:
- Each row represented a country
- Each column represented a year

To make the data suitable for analysis and visualization, the datasets were transformed into **tidy format** using `pandas.melt()`, resulting in:

- `geo`
- `name`
- `year`
- `gdpcapita` OR `mortality_rate`

This transformation ensures:
- Each row represents a single country–year observation
- The dataset can be easily merged
- The data structure follows tidy data principles

---

### 2.2 Merging the Datasets

The two tidy datasets were merged using an outer join on:

- `geo`
- `name`
- `year`

An outer merge was chosen to:
- Preserve all available observations
- Avoid unintentionally dropping countries or years

The final merged table contains:

- `geo`
- `name`
- `mortality_rate`
- `gdpcapita`
- `year`

---

### 2.3 Handling Missing Data

The following countries contained missing values:

- Andorra
- Dominica
- St. Kitts and Nevis
- Liechtenstein
- Marshall Islands
- Nauru
- Palau
- San Marino
- Tuvalu

For these countries, missing numerical values were replaced with `0`.

This choice was made because:
- Some countries were entirely missing from one dataset.
- The project instructions required explicitly addressing missing data.
- Replacing with zero allows these countries to remain in the dataset without causing merge or plotting errors.

---

## 3. Visualization Choices

### 3.1 Scatter Plot Design

A scatter plot was chosen because it is appropriate for examining the relationship between two continuous variables:

- X-axis: GDP per capita
- Y-axis: Child mortality rate
- Color: Year

Each point represents a single country-year observation.

---

### 3.2 Log Scale on GDP

GDP per capita spans several orders of magnitude across countries.  
To avoid compression of low-income countries and improve readability, the X-axis was transformed using a logarithmic scale.

This allows:
- Better visual separation of low- and middle-income countries
- A clearer representation of the economic gradient

---

### 3.3 Color Encoding of Time

Year was encoded using a continuous color scale.

This allows us to:
- Observe temporal progression
- Detect whether global mortality rates decrease over time
- Identify long-term development trends

---

## 4. Key Insights

The visualization reveals several important patterns:

### 4.1 Strong Negative Relationship

There is a clear inverse relationship between GDP per capita and child mortality rate:
- Countries with higher GDP per capita tend to have lower child mortality.
- Low-income countries exhibit significantly higher mortality rates.

This pattern aligns with well-established development economics findings.

---

### 4.2 Global Improvement Over Time

Color progression across years shows that:

- Earlier years are associated with higher mortality levels.
- Over time, most countries shift downward (lower mortality) and rightward (higher GDP).

This indicates:
- Economic growth
- Improvements in healthcare systems
- Better access to nutrition, sanitation, and vaccination

---

### 4.3 Diminishing Returns at High GDP Levels

At very high GDP levels:
- Mortality rates approach very low values.
- Additional GDP increases result in smaller reductions in mortality.

This suggests that beyond a certain development threshold, non-economic factors may play a larger role in further improvements.

---

## 5. Conclusion

This project demonstrates a clear and consistent relationship between economic development and child survival outcomes.

By transforming the raw data into tidy format, carefully merging datasets, addressing missing values, and selecting appropriate visualization techniques, we were able to uncover meaningful global patterns.

The analysis highlights the importance of economic development as a driver of public health improvements while also suggesting diminishing marginal returns at higher income levels.

---

## 6. Reproducibility

All data processing and visualization steps are implemented in Python scripts:

- `phase1_data_formatting.py`
- `phase2_visualization.py`

These scripts ensure that the entire workflow is reproducible and can be rerun if new data becomes available.
