"""Task 6: Data Visualization"""
"""Completed by Ananya Kavatekar"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parents[1]
processed = root / "data" / "processed"
figures = root / "figures"
figures.mkdir(exist_ok=True)

# Loading in the integrated dataset from prior steps
integrated = pd.read_csv(processed / "integrated.csv", parse_dates=["date"])

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