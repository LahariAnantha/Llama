# Data Cleaning Log

## 1. Overview

This document describes the data cleaning operations performed on the three datasets used in our project: the FRED Consumer Price Index (CPI), U.S. Census Monthly Retail Trade Survey (MRTS), and Bureau of Labor Statistics (BLS) unemployment rate.

The purpose of data cleaning is to identify and address initial data quality issues, standardize data formats, and prepare the datasets for further analysis.

Cleaning was performed using `scripts/clean_data.py`, which uses Python and pandas to process each dataset separately.

Original datasets are preserved in `data/raw/`, while cleaned versions are saved in `data/processed/`.

## 2. Initial Data Quality Assessment

The cleaning script identified the following data quality issues:

| Dataset | Original Records | Missing Values | Exact Duplicates | Duplicate Dates |
|---|---:|---:|---:|---:|
| FRED CPI | 957 | 1 | 0 | 0 |
| Census MRTS | 6,660 | 0 in selected records | 0 in selected records | 0 in selected records |
| BLS Unemployment | 33 | 1 | 0 | 0 |

The primary issues identified were missing numerical values, differences in data formats, and the presence of multiple statistical measures in the Census MRTS dataset.

For the MRTS dataset, 12 records matched the selected research variables. The remaining observations represented other categories or statistical measures and were excluded based on the project scope rather than data quality errors.

## 3. Data Cleaning Operations

### 3.1 FRED Consumer Price Index (CPI)

**Source File:** `data/raw/cpi.csv`

**Cleaned File:** `data/processed/cpi_clean.csv`

#### Issues Identified

- One observation contained a missing CPI value.
- Column names and data types required standardization.
- No duplicate records or duplicate dates were identified.

#### Cleaning Operations

1. Standardized column names to lowercase and renamed the variables to `date` and `cpi`.
2. Converted date values into a consistent datetime format.
3. Converted CPI values into numeric data types.
4. Removed the observation containing a missing CPI value.
5. Checked for invalid CPI values (values less than or equal to zero).
6. Verified that each reporting date appeared only once.
7. Sorted the dataset chronologically.

#### Results

- Original observations: 957
- Missing observations removed: 1
- Duplicate observations removed: 0
- Final observations: 956
- Date coverage: January 1947 – September 2026

#### Data Quality Improvements

These operations improved consistency by standardizing column names, data types, and dates. Removing the missing CPI observation ensured that all retained records contained valid values.

The validation checks also confirmed that the cleaned dataset did not contain duplicate reporting dates or nonpositive CPI values.

### 3.2 U.S. Census Monthly Retail Trade Survey (MRTS)

**Source File:** `data/raw/mrts.csv`

**Cleaned File:** `data/processed/retail_clean.csv`

#### Issues Identified

- The original dataset contained multiple retail categories and statistical measures.
- Different observations represented monthly sales, percentage changes, and other economic statistics.
- The dataset required filtering to select the series relevant to our research question.
- No missing values or duplicates were identified among the selected observations.

#### Cleaning Operations

1. Loaded the original MRTS CSV file using pandas.
2. Selected monthly sales observations using `data_type_code == "SM"`.
3. Filtered for Retail Trade and Food Services using `category_code == "44X72"`.
4. Selected seasonally adjusted observations using `seasonally_adj == "yes"`.
5. Excluded error statistics using `error_data == "no"`.
6. Converted the `time` column from `YYYY-MM` to `YYYY-MM-DD`.
7. Converted sales values into numeric format and renamed the column `sales_millions`.
8. Checked for missing values, exact duplicates, duplicate dates, and negative sales values.
9. Sorted the selected observations chronologically.

#### Results

- Original observations: 6,660
- Observations matching selected filters: 12
- Missing observations removed: 0
- Duplicate observations removed: 0
- Final observations: 12
- Date coverage: January 2025 – December 2025

#### Data Quality Improvements

Filtering the original dataset ensured that the cleaned data contained a consistent economic measure: seasonally adjusted monthly retail and food services sales in millions of dollars.

This prevented the analysis from mixing sales amounts with percentage changes or unrelated retail categories.

The reduction from 6,660 observations to 12 was due to selecting the relevant statistical series, not because the remaining records contained data quality errors.

Standardizing dates and numerical values improved consistency across datasets.

### 3.3 BLS Civilian Unemployment Rate

**Source File:** `data/raw/unemployment.json`

**Cleaned File:** `data/processed/unemployment_clean.csv`

#### Issues Identified

- The unemployment dataset was stored in nested JSON format.
- Year and month values required conversion to a common date format.
- One observation contained a missing or nonnumeric unemployment rate.
- No duplicate records or duplicate dates were identified.

#### Cleaning Operations

1. Extracted the `LNS14000000` unemployment series from the BLS JSON response.
2. Selected monthly observations using period values `M01` through `M12`.
3. Combined year and month fields into a standardized reporting date.
4. Converted unemployment values into numeric data types.
5. Identified one missing or nonnumeric unemployment observation for October 2025.
6. Removed the observation rather than replacing it with an estimated value.
7. Validated that remaining unemployment rates were between 0% and 100%.
8. Checked for duplicate reporting dates.
9. Sorted observations chronologically.

#### Results

- Original monthly observations: 33
- Missing observations removed: 1
- Duplicate observations removed: 0
- Final observations: 32
- Date coverage: January 2024 – September 2026, excluding October 2025

#### Data Quality Improvements

The cleaning operations improved consistency by transforming the nested JSON data into a standardized tabular format.

Removing the missing observation ensured that the cleaned dataset contained only valid numerical unemployment rates.

The missing value was not replaced with zero or an estimated value to avoid introducing unsupported information into the analysis.

## 4. Summary of Cleaning Results

| Dataset | Original Records | Selected Records | Missing Values Removed | Final Records |
|---|---:|---:|---:|---:|
| FRED CPI | 957 | 957 | 1 | 956 |
| Census MRTS | 6,660 | 12 | 0 | 12 |
| BLS Unemployment | 33 | 33 | 1 | 32 |

The cleaning process successfully standardized all three datasets and generated cleaned CSV files.

No exact duplicates or duplicate dates were identified in the assessed records.

## 5. Data Quality Dimensions Addressed

### Accuracy

- Converted numerical columns to appropriate data types.
- Checked CPI values for nonpositive observations.
- Checked retail sales for negative values.
- Validated that unemployment rates fell between 0% and 100%.

These checks identify invalid or implausible values but do not independently verify every observation against its original source.

### Completeness

- Identified and documented missing CPI and unemployment observations.
- Removed one missing CPI observation and one missing unemployment observation.
- Preserved a record of the number of observations removed during cleaning.

### Consistency

- Standardized column names across datasets.
- Converted reporting dates into a common format.
- Ensured numerical variables used consistent data types.
- Selected comparable monthly statistical measures for subsequent analysis.

### Timeliness

- Reviewed the date coverage of each cleaned dataset.
- Confirmed the availability of CPI observations through September 2026, retail observations through December 2025, and unemployment observations through September 2026.
- Identified differences in temporal coverage that must be considered during analysis.

Data cleaning does not independently establish whether the latest published observations have been acquired.

## 6. Remaining Limitations

Although the initial cleaning process was successful, some limitations remain.

The selected MRTS dataset contains only 12 monthly observations covering January through December 2025. This limits the time period available for analysis.

Additionally, the unemployment dataset contains a missing observation for October 2025. As a result, that month will not be available when using only complete observations across all three datasets.

These limitations will be considered when interpreting findings. The project will focus on exploratory associations rather than causal conclusions.

## 7. Reproducibility

All cleaning operations are implemented in:

`scripts/clean_data.py`

The cleaning process can be reproduced by running the following command from the root of the repository:

```bash
python scripts/clean_data.py
```

The script generates the following files:

- `data/processed/cpi_clean.csv`
- `data/processed/retail_clean.csv`
- `data/processed/unemployment_clean.csv`

The original source files remain unchanged in `data/raw/`, allowing cleaning operations to be reproduced and reviewed.