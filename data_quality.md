# Data Acquisition and Quality Assessment

## 1. Data Sources
The project uses three monthly economic datasets:
### FRED Consumer Price Index
- Dataset: CPI for All Urban Consumers
- Source: Federal Reserve Bank of St.Louis
- Frequency: Monthly
- File: data/raw/cpi.csv
- Purpose: Measure changes in consumer prices over time
### BLS Civilian Unemployment Rate
- Dataset: Civilian Unemployment Rate (LNS14000000)
- Source: US Bureau of Labor Statistics
- Frequency: Monthly
- File: data/raw/unemployment.json
- Purpose: Measure the civilian unemployment rate over time
### Census Monthly Retail Trade Survey
Dataset: Monthly Retail Trade Survey (MRTS)
- Source: US Census Bureau
- Frequency: Monthly
- File: data/raw/mrts.csv
- Purpose: Provide monthly retail trade measurements across different retail categories and data types. 

## 2. Data Acquisition
Data acquisition is performed programmatically using scripts/acquire_data.py. 

The scripts retrieves:
1. CPI data from FRED
2. Civilian unemployment data from the BLS Publi Data API.
3. MRTS data from the Census Bureau API.

The MRTS API requires a Census API key. The key is provided through the CENSUS_API_KEY environment variable and is not stored in the repository. 

To acquire the datasets run:
python scripts/acquire_data.py

This script saves the downloaded datasets to:
data/raw/cpi.csv
data/raw/unemployment.json
data/raw/mrts.csv 

Using a programmatic acquisition process makes the workflow reproducible and allows the datasets to be refreshed without manually downloading each file. 

## 3. Data Integrity Verification
SHA-256 checksums are used to verify that the downloaded files have not changed after acquisition. 
Integrity verification is implemented in:
scripts/verify_integrity.py 

To calculate and verify the checksums, run;
python scripts/verify_integrity.py

The checksums files are stored in:
data/checksums/ 
CPI: 8556b710094027fa4724641d48be620cc37c04abfa15a0c496378cf1146c1549
BLS Unemployment: 0684e2b33eb5cdc53cea3c5ac8579bad35bfa8586db61ec869050120e6976233
Census MRTS: 0a732bb8af80002d4e48c8f018e835158ff0898fc7cbfbe3d782a9637f0867fb

All 3 datasets passed the integrity check. 
The checksum files are:
data/checksums/cpi.sha256
data/checksums/unemployment.sha256
data/checksums/mrts.sha256
The checksums provide a way to detect whether a raw dataset has changed after it was acquired. 
## 4. Data Profiling
Data profiling is implemented in:
scripts/profile_data.py 
To run the profiling and quality checks:
python scripts/profile_data.py 

The profiling script checks for:
- Missing values
- Duplicate rows
- Duplicate observations
- Invalid dates
- Date ranges
- Missing Months
- Invalid Categorical values
- Non-numeric values
- Negative numeric values
- Minimum and maximum numeric values
- Dataset structure and data types 

## 5. Initial Quality Assessment
The datasets were evaluated across four quality dimensions: 
- Accuracy
- Completeness
- Timeliness
- COnsistency

### 5.1 FRED CPIAUCSL

#### Accuracy
The profiling checks found valid dates and non-negative CPI values. No duplicates were identified. The profiling process does not independently verify every CPI observation against an external ground-truth source. Therefore, accuracy is assessed primarily through internal validation.

#### Completeness
The CPI dataset contains 957 observations. There is one missing CPI value: October 2025
There were no duplicate rows or duplicate dates. 

#### Timeliness
The dataset covers January 1947 through September 2026. It therefore provides historical time series and includes recent observations. 

#### Consistency
Dates are valid and in chronological order. There are no duplicate dates, and the dataset follows a consistent structure consisting of the observation date and CPI value. 

### 5.2 BLS Civilian Unemployment Rate

#### Accuracy
The unemployment rate values are numeric for the available observations and fall within a reasonable range.

One observation contains - instead of a numeric unemployment rate for October 2025

This value is treated as an unavailable observation rather than a negative unemployment rate.
#### Completeness
The dataset contains 33 observations. There are no duplicate year-month observations. The latest filed contains many null values. This is expected behavior for the BLS API metadata and its not treated as missing unemployment data. 

#### Timeliness
The dataset covers January 2024 through September 2026 and therefore contains recent unemployment observations. 

#### Consistency
The year and motnh field are valid and can be converted into monthly dates. The BLS API returns observations from newest to oldest. This ordering is a characteristic of the API response and is not treated as a data-quality issue. 

### 5.3 Census Monthly Retail Trade Survey

#### Accuracy
The MRTS dataset contains both numeric measurements and source-provided special values.
The profiling identified:
6,200 numeric cell values
444 (S) values
16 Z values
The (S) and Z values are preserved because they are source-provided special values rather than automatically treating them as invalid data. The dataset also contains 544 negative numeric values. These values are not automatically classified as errors because the MRTS dataset contains different measures, and negative values may be meaningful for some measures. The profiling process does not independently verify every MRTS observation against an external ground-truth source, so accuracy is assessed primarily through structural and semantic checks.

#### Completeness
The MRTS dataset contains 6600 observations and has no null values across its 7 columns. There are no duplicate rows and no duplicate observations based on the combination of: 
- data_type_code
- time_slot_id
- seasonally_adj
- category_code
- time

#### Timeliness
The current MRTS dataset covers January 2025 through December 2025. This is shorter time span than the CPI and BLS datasets. Therefore, analyses using all 3 datasets together will be constrained by MRTS coverage period. 

#### Consistency
The MRTS data contains consistent date formatting and valid values for the seasonally_adj and error_data fields. 
There are:
- 10 unqiue data type codes
- 64 unique category code
- 0 invalid seasonally_adj values
- 0 invalid error_data values

The Census API response is grounded by data series, so the overall dataset is not globally chronological. This is an API response-order characteristic and is not treated as a data-quality problem. 


## 6. Integration Feasibility

The three datasets are feasible to integrate for monthly economic analysis, but they require preprocessing because their schemas and measurements differ. A common monthly time key can be created for all 3 datasets:
- CPI uses observaion_date
- BLS uses year and period
- MRTS uses the time field 

The datasets do not have identical coverage periods. CPI and BLS contain longer historical periods, while the current MRTS extract covers 2025. When integrating the datasets, the project should: 
1. Convert all date fields to a commong monthly date formal.
2. Keep the original raw datasets unchanged.
3. Handle missing or unavailable observations explicitly.
4. Preserve source-provided MRTS special values such as (S) and Z.
5. Avoid interpreting negative MRTS values as errors without considering the associated data type and measure.
6. Ensure that MRTS categories and data type codes are not accidentally combined across different measures.
7. Document any filtering, transformation, or imputation performed during downstream analysis.

The datasets are suitable for integration, particularly for explanatory monthly analysis, but the should not simply be concatenated because each source uses a different schema and represents different economic measures. 

## 7. Identified Data Quality Issues
The initial profiling identified the following issues and considerations:

CPI - One missing value is October 2025 - Should be handled explicitly during integration
BLS - October 2025 value is "-" - Treat as unavailable rather than numeric 
BLS - latest field contains nulls - Expected API metadata behavior 
MRTS - 444 (S) values - Source provided special value; preserve and interpret 
MRTS - 16 Z values - No automatically errors; interpretation depends on measure 
All datasets - Different time coverage - Must be considered when integrating 
No duplicate rows or duplicate observations were identified in any of the 3 datasets. 

## 8. Overall Assessment
Overall, the datasets are sufficiently structured for integration and further analysis. The acquisition workflow is reproducible, the downloaded files have been verified using SHA-256 checksums, and the profiling scripts identify missing values, duplicates, inconsistencies, and potential data quality issues. The main considerations for downstream analysis are the missing or unavailable observations, source-specific MRTS special values, different time coverage periods, and differences in measurement definitions. These issues can be addressed during the data integration and preprocessing stage without preventing the datasets from being used for further analysis. 
