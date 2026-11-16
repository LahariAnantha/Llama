## Changes to Project Plan 
Our project is currently on track with the original project plan, and we have not needed to make any changes to the planned timeline or overall approach. 

## Lahari Anantha — Contributions to Current Milestone

For this milestone, I focused on data cleaning, repository organization, and technical documentation to prepare our datasets for further analysis.

Tasks Completed:

Data Cleaning Scripts: Developed scripts/clean_data.py to clean and standardize the CPI, MRTS, and unemployment datasets. Implemented data type conversions, date standardization, missing-value handling, duplicate detection, and validation checks. The script successfully generated cleaned versions of all three datasets in data/processed/.

Repository Structure and Documentation: Updated README.md to document the GitHub repository's structure, file organization, naming conventions, and the purpose of each script and dataset. Established documentation outlining how raw data, processed data, and project scripts are organized to support reproducibility.

Cleaning Operations Documentation: Created cleaning_log.md to document the cleaning procedures performed on each dataset, including the data quality issues identified, transformations applied, and resulting improvements. Recorded the number of observations before and after cleaning and explained decisions regarding missing values and data filtering.

Conceptual Integration Schema: Developed integration_schema.md to document the structure of the three datasets, their key attributes, and the common monthly date field that establishes relationships between them. Defined a consistent schema to support subsequent analysis.

Challenges and Resolutions:

One challenge involved differences in the formats of the three source datasets. The CPI data was provided as a CSV, MRTS contained multiple categories and statistical measures, and unemployment data was stored in JSON format. I addressed these differences by developing dataset-specific cleaning functions that standardized column names, dates, and numerical values.

Another challenge involved missing observations. The initial quality checks identified one missing CPI value and one missing unemployment rate for October 2025. These observations were excluded rather than estimated to avoid introducing unsupported values. Additionally, the MRTS dataset contained 6,660 records across multiple statistical categories, requiring filtering to retain the 12 seasonally adjusted monthly retail and food services sales observations relevant to our research scope.

Progress and Next Steps:

The initial cleaning scripts have been implemented and successfully tested, producing 956 cleaned CPI observations, 12 retail sales observations, and 32 unemployment observations. The repository structure, cleaning operations, and conceptual schema have also been documented. My remaining work includes reviewing the documentation for consistency with the implemented scripts and making any necessary refinements based on team feedback.


## Anjali Penamutcha — Contributions to Current Milestone
For this milestone, I focused on data acquisition, data integrity verification, data profiling, and technical documentation to prepare our datasets for integration and further analysis. 

Tasks Completed:
Programmatic Data Acquisition: Developed scripts/acquire_data.py to programmatically retrieve the CPI, unemployment, and Monthly Retail Trade Survey(MRTS) datasets. The script downloads the CPI data from FRED, retrieves the civilian unemployment rate through the BLS API, and retrieves MRTS data through the Census API. The datasets are stored in /raw/ to maintain a consistent repository structure. 

Data Integrity Verification: Developed scripts/verify_integrity.py to calculate and verify SHA-256 checksums for each raw dataset. Checksum files are stored in data/checksums/. All 3 datasets successfully passed the initial integrity checks, providing a way to detect changes to the raw data after acquisition. 

Data Profiling and Quality Assessment: Developed scripts/profile_data.py to profile the CPI, unemployment, and MRTS datasets. The script checks for missing values, duplicate rows, duplicate observations, invalid dates, date ranges, categorical inconsistencies, non-numeric values, and numeric value ranges. The profiling results were used to evaluate the datasets across the 4 required quality dimensions: accuracy, completeness, timeliness and consistency. 

Quality Assessment Documentation: Created data_quality.md to document the data sources, acquisition workflow, integrity verification process, profiling procedures, identified quality issues, and integration feasibility. The documentation also records dataset-specific limitations, including the missing CPI observation, unavailable BLS observation, source-provided special values in the MRTS dataset. 

Data Challenges and Resolutions 
One challenge involved differences in the formats and structures of the three source datasets. The CPI data is provided as a CSV, the BLS data is returned as JSON, and the MRTS data is returned through the Census API as a multi-series dataset. I addressed these differences by creating dataset-specific acquisition and profiling procedures while maintaining a consistent raw-data folder. The MRTS dataset presented an additional challenge because it contains multiple data types and retail categories. The profiling identified 6600 observations, including source-provided (S) and Z values and negative numeric values. These values were not automatically removed because their meaning depends on the specific MRTS measure. 

Progress and Next Steps 
The data acquisition, integrity verification, and profiling workflows have been implemented and test successfully. The 3 raw datasets have been acquired and stored in the repository, SHA-256 checksums have been generated and verified, and initial data quality issues have been identified and documented. My remaining work includes reviewing the documentation for consistency with the implemented scripts, making any necessary refinements based on team feedback. 


### Mihika Johar — Contributions to Current Milestone

For this milestone, I focused on researching and documenting our three economic datasets: the Consumer Price Index (CPI), Monthly Retail Trade Survey (MRTS), and Civilian Unemployment Rate. I developed initial data profiles outlining their sources, formats, and characteristics, reviewed ethical and legal considerations, and examined how each dataset relates to our research question. I also identified year and month as the common attributes for integration, researched relevant academic literature, and selected the DataONE Data Life Cycle Model to guide our data management process.

Challenges and Resolutions

One challenge was determining how datasets from three different government sources could be meaningfully integrated, given their different structures, formats, and economic measures. I addressed this by identifying their shared monthly time dimension and examining how each dataset contributes to our research question about inflation, unemployment, and consumer spending.

Another challenge was understanding the limitations of using aggregated economic statistics, particularly differences in data coverage, measurement methods, and seasonal adjustments. To address this, I documented these limitations and identified areas requiring further verification, including source-specific licensing conditions and compatibility across datasets.

Progress and Next Steps

The initial dataset research, literature review, and selection of the data lifecycle model have been completed. My next steps include verifying source-specific licensing requirements, reviewing the compatibility of the datasets' time periods and seasonal adjustments, and supporting the team's data integration and analysis process. I will also help ensure that our final analysis acknowledges the limitations of the datasets and avoids drawing unsupported causal conclusions.


### Ananya Kavatekar - Contribution to Current Milestone

For this milestone, I focused on integrating the three cleaned economic datasets (consumer price index, unemployement rate, and retail sales), assured the integration efficacy through quality and completeness checks, and performed some initial exploratory data analysis to explore the relationship between inflation indicated by the consumer price index, the unemployment rate, and consumer spending through retail sales.

Data Integration: 

Developed scripts/integrate_data.py to integrate the cleaned CPI, retail sales, and unemployment datasets using Python and pandas. I first loaded the three cleaned CSV files, converting their date columns into datetime objects using parse_dates. Since all three datasets contained monthly observations with a common date attribute, I used two inner joins to combine them. The first joined retail sales with CPI, while the second added unemployment data. Inner joins ensured that only months present in all three datasets were retained. I then selected the four relevant columns (date, cpi, unemployment_rate, and sales_millions) and saved the resulting 11 observations to data/processed/integrated.csv. October 2025 was excluded because it was not available across all three cleaned datasets.

The dataset is called integrated.csv and is under the data/processed folder. It contains 11 monthly observations from 2025.

Post-Integration Data Quality Assessment:

Within the integrate_data.py script I also included checks for missing values (date, cpi, unemployment, sales), duplicate observations, and date range. Through the review of the table outputted by these checks I affirmed that the dataset contained 0 missing values, 0 duplicates, and the date range encompassed the entire year affiriming the completeness of the dataset as well (except Oct 2025 is incomplete due to it not being present in the CPI dataset). 

Exploratory Data Analysis: 

After confirming the quality and completeness of the integrated dataset I utilized the dataset to calculate the descriptive statistics and Pearson correlations for the three economic metrics. This analysis found that there is a positive correlation of 0.88 between Consumer Price Index and Retail Sale and a positive correlation of 0.73 between unemployment rates and retail sales. 

Visualizations: 

Fromt the dataset, I generated a CPI vs. Retail Sales scatterplot to explore the relationship between the two metrics across 2025 and also created a more complex multi-graph visualization that compares the trendline of all three metrics throughout 2025 to explore more on how each independently moved in 2025 and compare the similarity and dissimilarity of those movements.
These visualizations are called cpi_vs_sales.png and monthly_metric_trends.png respectively and are under the figures folder.

The visualizations revealed that CPI and retail sales generally increased across the year 2025, while unemployment fluctuated between 4.0% 4.5% and that all the metrics peaked at December 2025. 


Challenges and Resolutions: 

One challenge was the slight difference in observation counts and date coverage across the datasets due to October 2025 not being present in the cleaned CPI and unemployment datasets. For that reason, I used inner joins to retain only months with complete observations rather than estimating the missing values.

Progress and Next Steps:

The data cleaning, integration, inital analysis, and visualization have now been completed and tested. Tasks for the next milestone could include expanding the dataset date range and further conducting deeper analysis to better understand the relationships between economic conditions and consumer spending via the datasets created getting closer to answering the core research question. 
