# Project Plan

## 1. Research Question

**Main Research Question:**

How are the inflation rate (represented by the Consumer Price Index) and unemployment rate associated with changes in consumer spending in the food and retail categories in the United States?

## 2. Datasets

We will use the following three datasets to investigate the relationship between inflation, unemployment, and consumer spending.

1. **Federal Reserve Economic Data (FRED)**
   - **Dataset:** Consumer Price Index for All Urban Consumers (CPIAUCSL)
   - **Source:** [FRED — Consumer Price Index](https://fred.stlouisfed.org/series/CPIAUCSL)
   - **Purpose:** Measure changes in consumer prices and inflation over time.

2. **U.S. Census Bureau**
   - **Dataset:** Monthly Retail Trade Survey (MRTS)
   - **Source:** [U.S. Census — Monthly Retail Trade](https://www.census.gov/retail/index.html)
   - **Purpose:** Analyze changes in consumer spending across food and retail categories.

3. **U.S. Bureau of Labor Statistics (BLS)**
   - **Dataset:** Civilian Unemployment Rate (LNS14000000)
   - **Source:** [BLS — Unemployment Rate](https://data.bls.gov/timeseries/LNS14000000)
   - **Purpose:** Examine the relationship between unemployment and consumer spending patterns.

## 3. Project Timeline

### October 12–17: Further Research on Our Datasets

- [ ] Create a data profile for each dataset, describing its structure, content, characteristics, and repository location.
- [ ] Discuss ethical and legal constraints, including licensing and terms of use.
- [ ] Explain how the three datasets relate to our research question and identify common attributes that allow integration.
- [ ] Find related research papers or other relevant literature.
- [ ] Identify a data lifecycle model applicable to our project.

### October 19–24: Data Acquisition and Initial Data Quality Assessment

- [ ] Create scripts to programmatically acquire data and verify integrity using SHA-256 checksums.
- [ ] Create documentation describing how to acquire data and verify integrity.
- [ ] Assess each dataset across four quality dimensions: accuracy, completeness, timeliness, and consistency.
- [ ] Create scripts to profile datasets and identify missing values, duplicates, inconsistencies, and other quality issues.
- [ ] Document initial quality assessment results and the feasibility of integrating the datasets.

### October 26–31: Data Storage, Organization, and Initial Cleaning

- [ ] Create scripts to load data into a relational database, if applicable.
- [ ] Document the structure and naming conventions of project files and the GitHub repository.
- [ ] Create Python or SQL scripts to address initial data quality issues.
- [ ] Document cleaning operations and explain how they address problems identified during the quality assessment.
- [ ] Develop a conceptual ER model or integration schema identifying relationships between the datasets.
- [ ] Begin developing the automated workflow.

### November 2–13: Data Cleaning, Integration, and Initial EDA

- [ ] Complete data cleaning scripts and document the cleaning operations performed.
- [ ] Create scripts to integrate all three datasets using Python or SQL.
- [ ] Document the integration process, including common attributes and join methods.
- [ ] Conduct a post-integration data quality assessment covering accuracy, completeness, timeliness, and consistency.
- [ ] Begin exploratory data analysis using the integrated dataset.
- [ ] Generate preliminary numeric findings and at least one visualization.

### November 16–20: Further Data Analysis, Workflow Automation, and Interim Report

- [ ] Complete additional data analysis and visualizations.
- [ ] Finalize documentation describing the steps used to analyze and visualize data.
- [ ] Create a Snakemake workflow or run-all script automating the end-to-end process from data acquisition through analysis.
- [ ] Document the steps required to execute the workflow.
- [ ] Complete the interim status report, including progress, challenges, updated timeline, and individual contributions.
- [ ] **Submit the interim status report by November 19.**

### November 23–29: Finalizing Analysis and Project Documentation

- [ ] Finalize analysis results and visualizations.
- [ ] Complete the required README sections, including findings, challenges, future work, and references.
- [ ] Create a data dictionary documenting variables across the datasets.
- [ ] Create a machine-readable metadata file using DCAT, DataCite, or Schema.org.
- [ ] Ensure all scripts, datasets, and project artifacts are organized and linked in the repository.

### November 30–December 6: Reproducibility Testing and Final Submission Preparation

- [ ] Finalize the reproducible package, including `requirements.txt` and specific software versions.
- [ ] Include appropriate licenses for the datasets and software.
- [ ] Test the entire workflow from a fresh clone of the GitHub repository.
- [ ] Verify that all scripts run without errors, use relative paths, and reproduce the expected outputs.
- [ ] Review the final README to ensure all required sections, references, and artifact links are included.
- [ ] Create the final GitHub release and prepare the submission for **December 7**.



Why this format works better
- Headings (#, ##, ###) make it
