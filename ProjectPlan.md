# Project Plan

## Overview

This project aims to explore how inflation and unemployment rate are associated with changes to consumer spending trends for food and retails goods. Particularly, this project will inspect inflation through the lens of changing price points for common and routine consumer purchases via the consumer price index and along with employment rates attempt to analyze whether these economic indicators provide insight to spending behaviors in the retail and food category.   

To research the relationship between these variables, three publicly accessible datasets hosted by government entities including the Federal Reserve Economic Data (FRED), U.S. Census Bureau, and Bureau of Labor Statistics will be used. These datasets provide monthly insights on the consumer price index, retail and food spending, and the civilian unemployment rate. The datasets acquired from these reputable sources will be documented, assessed for quality and missing values, and cleaned. The datasets will then be filtered to a chosen common time period and then be analyzed to study correlation or relationship between these economic indicators. The seasonal adjustment factors will also be analyzed to explore how this relationship between metrics may vary across routine time periods.

The main objective is to produce a sound workflow for extracting, processing, integrating, and analyzing economic data from multiple government platforms to better understand how consumer spending habits vary in differing economic conditions. 

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
  
## 2b. Dataset Descriptions

Dataset 1: Consumer Price Index for All Urban Consumers (CPIAUCSL)

This dataset contains the monthly consumer price index focused particularly on consumers living in metropolitan areas in the United States. The consumer price index provided the weighted average price changes to a set of consumer goods and services that are expected purchases for American households across lifetimes. It is a measure for evaluating the change of expenses and possibly strain that American consumers face in differing economic conditions. This dataset is from the Federal Reserve Economic Data site published and maintained by the Federal Reserve Bank of St. Louis. It is available through CSV format or direct access via API. There are two primary fields in this dataset: DATE and CPIAUCSL. The date is presented in the standard YYYY-MM-DD format and the CPI (consumer price index) are floats (numbers including decimals). The base prices for the CPI are drawn from 1982-1984. 

Dataset 2: Monthly Retail Trade Survey (MRTS)

This dataset contains monthly estimates of retail and food sales across the United States starting from 1992 to present day. The dataset is presented in a .txt file that contains two main sections. First a white-space separated table that contains the retail and food sales spending by year and month as a whole integer in millions of dollars. The second table presents the seasonal adjustment factor by year and month as a float. This figure provides consideration to natural ebbs and flows in consumer spending during seasonal events/periods (i.g. holidays). 

Dataset 3: Civilian Unemployment Rate (LNS14000000)

This dataset provides the monthly unemployment rate published by the United States Bureau of Labor Statistics (BLS) for the United States civilian labor force aged 16 and above. The data is presented in table form via a HTML with access to export as .xlsx file.The data table is in wide format with years (integers) as rows and twelve columns representing months. The unemployment rate by year and month is stored as floats (numbers containing decimals) which represent the percentage of the civilian population that has been surveyed to be unemployed. The data ranges from 2016 to 2026 and is modified to consider seasonal adjustment figures. 

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

## 4. Team 
Our team will divide responsibilities between the technical implementation and written documentations, where 2 team members will primarily focus on the technical components and the other 2 team members will focus on the documentation and reporting aspects of the project. The technical team will work on things like data acquisition, SHA-256 integrity verification, data profiling, exploratory data analysis, visualization and workflow automation. The documentation team will work on the data profiles, research on ethical and legal constraints, integration schema documentation, data dictionary and project reports. All of us will collaborate to interpret findings, identify challenges, and ensure the documentation accurately reflects the technical work. We will make sure that all the documentation and reports are in line with the technical work by having meetings where we discuss the technical decision we took and the reasoning behind it. The documentation and reporting team will also keep us updated on any coding that seems unethical and violates any of our constraints. We will all collaborate on the README, reviewing the repository and preparing the final submission. 

## 5. Constraints 
This project relies on three publicly available government datasets that measure different aspects of the economy. One limitation is that the Consumer Price Index (CPI) represents price changes experienced only by urban consumers. Therefore, it may not fully represent the price experiences and spending patterns of rural consumers and all demographic groups. Additionally the CPI is calculated using sampled pieces rather than prices from every transaction, making the estimates subject to sampling error. Because the index includes food and energy prices, even small-term fluctuations can complicate the interpretation of underlying inflation trends. Therefore the analysis can only establish associations between these economic indicators but cannot prove causation. Inflation and employment are not the only factors affecting consumer spending. Changes in things like wages, interest rates and consumer confidence and seasonal shopping patterns can also cause changes in retail sales. Another limitation is that the Census Monthly Retail Trade Survey measures sales in dollar amounts rather than the quantity of goods purchased. Increases in small retail sales may reflect higher prices rather than an actual increase in purchasing activity. The datasets also have different definitions, unit and reporting procedures, which require a careful alignment of dates and consistent data preprocessing. Seasonal patterns may affect prices, sales and unemployment measurements differently, so we will need to verify the seasonal adjustment status of each series before comparing them. 

