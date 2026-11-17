
"""Initial Data Analysis"""
"""Completed by Ananya Kavatekar"""

from pathlib import Path
import pandas as pd

root = Path(__file__).resolve().parents[1]
processed = root / "data" / "processed"

# Loading in the integrated dataset from the previous step
integrated = pd.read_csv(processed / "integrated.csv", parse_dates=["date"])

# EDA - data summarizations
eda_vars = ["cpi", "unemployment_rate", "sales_millions"]

summary = integrated[eda_vars].describe().round(2)
correlations = integrated[eda_vars].corr().round(2)

print("\nSummary Statistics:")
print(summary)

print("\nCorrelations:")
print(correlations)

# Saving analysis results to csv within the data/processed folder 
summary.to_csv(processed / "summary_statistics.csv")
correlations.to_csv(processed / "correlations.csv")