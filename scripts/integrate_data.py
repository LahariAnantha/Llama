"""Task 4: Data Integration and Initial EDA"""
"""Completed by Ananya Kavatekar"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

#
root = Path(__file__).resolve().parents[1]
processed = root / "data" / "processed"
figures = root / "figures"
figures.mkdir(exist_ok=True)


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

# EDA - data summerizations
eda_vars = ["cpi", "unemployment_rate", "sales_millions"]

print("\nSummary Statistics:")
print(integrated[eda_vars].describe().round(2))

print("\nCorrelations:")
print(integrated[eda_vars].corr().round(2))


# Viz - Consumer Price Index vs Retail Sales

plt.scatter(integrated["cpi"], integrated["sales_millions"])

plt.xlabel("Consumer Price Index (CPI)")
plt.ylabel("Retail Sales (Millions of Dollars)")
plt.title("CPI vs Retail Sales (2025)")

plt.tight_layout()
plt.savefig(figures / "cpi_vs_sales.png")
plt.close()


# Viz - Unemployment rate vs Retail Sales

# turning the date column into an index, force the dataset to have only 1 row for the start of each month present
month_start = integrated.set_index("date").asfreq("MS")

axes = month_start.plot(
    subplots=True,
    figsize=(10, 8),
    marker="o",
    legend=False
)

axes[0].set_ylabel("CPI")
axes[1].set_ylabel("Unemployment (%)")
axes[2].set_ylabel("Sales ($ millions)")
axes[2].set_xlabel("Month")

plt.suptitle("2025 CPI, Unemployment, and Retail Sales Trend")
plt.tight_layout()
plt.savefig(figures / "monthly_metric_trends.png")
plt.close()