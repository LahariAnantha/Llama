## Updated Project Timeline

### November 23–29: Final Analysis and Documentation

**Remaining Tasks:**
- Finalize data analysis and visualizations.
- Interpret findings on the relationship between inflation, unemployment, and consumer spending.
- Create a data dictionary documenting variables across the datasets.
- Develop a machine-readable metadata file using DCAT, DataCite, or Schema.org.
- Update `README.md` with findings, challenges, limitations, and references.
- Review and finalize all project documentation.
- Ensure all scripts, datasets, and artifacts are properly organized and linked in the repository.

**Artifacts:**
- [README.md](README.md)
- [data_quality.md](data_quality.md)
- `data_dictionary.md` (to be created)
- Machine-readable metadata file (to be created)
- Final analysis scripts and visualizations (to be created)
- Finalized `data/processed/integrated.csv`


### November 30–December 6: Reproducibility Testing and Final Submission

**Remaining Tasks:**
- Test the full workflow from a fresh GitHub repository clone.
- Verify that all scripts execute successfully using relative paths.
- Finalize `requirements.txt` with Python dependencies and version numbers.
- Confirm that the workflow reproduces the expected datasets and outputs.
- Review the final README and documentation for completeness.
- Verify that all team contributions are committed to GitHub.
- Create the final GitHub release and prepare the submission.

**Artifacts:**
- [run_all.py](scripts/run_all.py)
- [README.md](README.md)
- `requirements.txt`
- Final reproducible datasets and analysis outputs
- Final GitHub release (to be created)

**Expected Completion:** December 6, 2026  
**Final Submission Due:** December 7, 2026


## Changes to Project Plan 
Our project is currently on track with the original project plan, and we have not needed to make any changes to the planned timeline or overall approach. 

## Challenges Overview 
Majority of our challenges were related to to data acquisition, cleaning, and integration. This primarily happened because our three datasets came from different government sources, which has different formats, structures, and measurement methods, which made it difficult to directly combine them. We tried to tackle this by developing dataset-specific scripts to standardize the given column names, date formats, and numerical values. Another big challenge we faced was handling missing observations, particularly for October 2025 in the CPI and unemployment datasets. Instead of estimating missing values, we chose to excluded incomplete months during integration, resulting in 11 complete monthly observations instead. Additionally, the MRTS dataset contained thousands of records across different categories, this included special values that needed careful interpretation. We addressed this part by  profiling the data and filtering it so that it only retains relevant  observations. We also did validation checks for missing values, duplicates, and inconsistencies to ensure the consistency and quality. Finally, the differences in data coverage and seasonal adjustments brought us challenges when interpreting relationships between economic indicators. We documented these limitations and identified areas that will need further verification before we conduct deeper analysis.

## Lahari Anantha — Contributions to Current Milestone

For this milestone, I mainly worked on data cleaning and documentation to make sure our datasets were consistent and ready for further analysis.

### Tasks Completed

- **Data Cleaning Scripts:** I developed `scripts/clean_data.py` to clean the CPI, MRTS, and unemployment datasets. This included standardizing dates and column names, converting values into the correct data types, checking for duplicates, and handling missing values. The script successfully generated cleaned versions of all three datasets in `data/processed/`.

- **Repository Structure and Documentation:** I updated `README.md` to explain how our GitHub repository is organized, including the purpose of each folder, script, and dataset. I also added file naming conventions to make the repository easier to navigate and understand.

- **Cleaning Operations Documentation:** I created `cleaning_log.md` to explain the cleaning steps performed on each dataset and how they addressed the data quality issues we identified. I also included the number of observations before and after cleaning and explained why certain values were removed or filtered out.

- **Conceptual Integration Schema:** I created `integration_schema.md` to outline the structure of our three datasets and identify the common date attribute they share. This helps explain how the datasets relate to one another and how they can be used together for our analysis.

### Challenges and Resolutions

One challenge I faced was that our three datasets had different formats. CPI was stored as a CSV, MRTS contained multiple categories and statistical measures, and unemployment was stored as a JSON file. To address this, I created separate cleaning functions for each dataset to make sure the dates, column names, and values were standardized.

Another issue was identifying missing values in our datasets. We found one missing CPI value and one missing unemployment rate for October 2025. I removed these observations rather than filling them with estimated values to avoid introducing inaccurate data. I also had to filter the MRTS dataset, which originally contained 6,660 records, to select the 12 monthly observations that were relevant to our research question.

### Progress and Next Steps

So far, I have completed and tested the cleaning script, which resulted in 956 CPI observations, 12 retail sales observations, and 32 unemployment observations. I also completed the repository documentation, cleaning log, and conceptual integration schema.

Moving forward, I plan to review the documentation to make sure everything matches our current scripts and make any necessary updates based on team feedback.

## Anjali Penamutcha — Contributions to Current Milestone
For this milestone, I focused on data acquisition, data integrity verification, data profiling, and technical documentation to prepare our datasets for integration and further analysis. 

Tasks Completed:
- Developed scripts/acquire_data.py to programmatically retrieve the CPI, unemployment, and MRTS datasets from FRED, the BLS API, and the Census API, respectively. The datasets are stored in data/raw/.
- Developed scripts/verify_integrity.py to calculate and verify SHA-256 checksums for all three datasets. All datasets passed the initial integrity checks.
- Developed scripts/profile_data.py to assess missing values, duplicates, invalid dates, categorical inconsistencies, non-numeric values, and numeric ranges. These results were used to evaluate accuracy, completeness, timeliness, and consistency.
- Created data_quality.md documenting the data sources, acquisition and integrity workflows, profiling results, identified issues, and integration feasibility.

Data Challenges and Resolutions 
The 3 datasets differ in format and structure, with CPI provides as CSV, BLS as JSON and MRTS as a multi-series Census API dataset. Dataset-specific acquisition and profiling procedures were used to account for these differences. MRTS also contains source-provided special values and negative values, which were documented rather than automatically removed because their meaning depends on the specific measure. 

Progress and Next Steps 
The data acquisition, integrity verification, and profiling workflows have been implemented and tested, and the identified quality issues have been documented. The remaining work is to review the documentation for consistency with the scripts and make any necessary refinements based on team feedback. 

### Mihika Johar — Contributions to Current Milestone

For this milestone, I focused on researching and documenting our three economic datasets: the Consumer Price Index (CPI), Monthly Retail Trade Survey (MRTS), and Civilian Unemployment Rate. I developed initial profiles outlining their sources, formats, and characteristics, reviewed ethical and legal considerations, and evaluated how each of our datasets relate to our research question. I also figured year and month as the common attributes for integration, researched relevant academic literature, and selected the DataONE Data Life Cycle Model to guide our data management process.

Challenges and Resolutions

A big challenge was determining how 3 different government sourced datasets could be integrated, since they had  different structures, formats, and economic measures. I addressed this by identifying their shared monthly time dimension and then examined the overlaps and contributions it gave to our research question. 

Another challenge I faced was understanding the limitations of using aggregated economic statistics, particularly differences in data coverage, measurement methods, and seasonal adjustments. I documented these limitations and identified areas requiring further verification, including source-specific licensing conditions and compatibility  to address this. 

Progress and Next Steps

The initial dataset research, literature review, and selection of the data lifecycle model have been completed. My next steps include verifying source-specific licensing requirements, reviewing the compatibility of the time periods and seasonal adjustments, and supporting the team's data integration and analysis process by making sure we avoid drawing unsupported causal conclusions.


### Ananya Kavatekar - Contribution to Current Milestone

For this milestone, I focused on integrating the three cleaned economic datasets (consumer price index, unemployement rate, and retail sales), assured the integration efficacy through quality and completeness checks, and performed some initial exploratory data analysis to explore the relationship between inflation indicated by the consumer price index, the unemployment rate, and consumer spending through retail sales.

Data Integration: 

Developed scripts/integrate_data.py to integrate the cleaned CPI, retail sales, and unemployment datasets using the pandas library. I loaded the three cleaned CSV files, and transformed their date columns into datetime objects using parse_dates. As all three datasets contained monthly observations with a common date attribute. I used two inner joins to combine them. The first joined retail sales with CPI, and the second added unemployment data. Inner joins ensured that only months present in all three datasets were retained. I then filtered to the four relevant columns (date, cpi, unemployment_rate, and sales_millions) and saved the resulting 11 observations to data/processed/integrated.csv. October 2025 was excluded because it was not available across all three cleaned datasets.

Post-Integration Data Quality Assessment:

Within the integrate_data.py script I included checks for missing values (date, cpi, unemployment, sales), duplicate observations, and date range. Through reviewing the output it's affirmed that there are 0 missing values, 0 duplicates, and the date range encompassed the entire year except Oct 2025 marking high completeness of the dataset. 

Exploratory Data Analysis: 

I calculated summary statistics for the integrated dataset along with Pearson correlations for the three economic metrics. This found a positive correlation of 0.88 between Consumer Price Index and Retail Sale and a positive correlation of 0.73 between unemployment rates and retail sales. 

Visualizations: 

I created two visualizations. 'CPI vs. Retail Sales' (data/figures/cpi_vs_sales.png) scatterplot explored the relationship between the two metrics across 2025 and '2025 CPI, Unemployment, and Retail Sales Trend'(data/figures/monthly_metric_trends.png) showcases the trend of all three metrics throughout 2025 independently. The visualizations revealed that CPI and retail sales generally increased across the year 2025, while unemployment fluctuated between 4.0% 4.5%, and all the metrics peaked in December. 


Challenges and Resolutions: 

October 2025 was missing from the cleaned CPI and unemployment dataset, creating a slight difference in data coverage. To resolve, I used inner joins to retain only observations present in all three datasets.

Progress and Next Steps:

Data cleaning, integration, initial analysis, and visualizations are complete and tested. Future tasks could include expanding the dataset date range and further conducting deeper analysis to better understand the relationships between economic conditions and consumer spending. 
