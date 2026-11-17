"""Task 4: Data Integration and Initial EDA"""
"""Completed by Ananya Kavatekar"""

from pathlib import Path
import pandas as pd

#
root = Path(__file__).resolve().parents[1]
processed = root / "data" / "processed"


# Loading in the cleaned datasets from prior steps
cpi = pd.read_csv(processed / "cpi_clean.csv", parse_dates=["date"])
retail = pd.read_csv(processed / "retail_clean.csv", parse_dates=["date"])
unemployment = pd.read_csv(processed / "unemployment_clean.csv", parse_dates=["date"])


# Integrating datasets by dates 
## The cleaned datasets are already sorted chronologically so no additional work needed for that

# inner joining the consumer pricing index and retail dataset by date 
integrated = retail.merge(cpi, on="date", how="inner")

# inner joining integrated dataset with unemployment data on date
integrated = integrated.merge(unemployment, on="date", how="inner")

# filtering integrated dataset to only the relevant columns  
integrated = integrated[["date", "cpi", "unemployment_rate", "sales_millions"]]


# Data Quality Checks for the integrated dataset
## making sure there is not any months and values missing from the integrated dataset
missing_months = retail.loc[~retail["date"].isin(integrated["date"]), "date"]
print("Integrated rows:", len(integrated))
print("Missing months:", missing_months.dt.strftime("%Y-%m").tolist())
print("Missing values:")
print(integrated.isna().sum())
print("Duplicate dates:", integrated["date"].duplicated().sum())
print("Date range:", integrated["date"].min(), "to", integrated["date"].max())


# saving the integrated dataset to a csv in the processed subfolder in the data folder
integrated.to_csv(processed / "integrated.csv", index=False)