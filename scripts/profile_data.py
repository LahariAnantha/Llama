import pandas as pd
import json
from pathlib import Path

RAW_DATA_DIR = Path("data/raw")

CPI_FILE = RAW_DATA_DIR / "cpi.csv"
UNEMPLOYMENT_FILE = RAW_DATA_DIR / "unemployment.json"
MRTS_FILE = RAW_DATA_DIR / "mrts.csv"


def load_cpi_data():
    """Load the CPI dataset."""
    df = pd.read_csv(CPI_FILE)
    return df


def load_unemployment_data():
    """Load the BLS unemployment dataset and extract observations."""
    with open(UNEMPLOYMENT_FILE, "r") as file:
        data = json.load(file)

    series = data["Results"]["series"][0]
    df = pd.DataFrame(series["data"])
    return df


def load_mrts_data():
    """Load the Census MRTS dataset."""
    df = pd.read_csv(MRTS_FILE)
    return df


def profile_cpi(df):
    """Display basic information about the CPI dataset."""
    print("CPI Dataset Profile")
    print("-------------------")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print()
    print("Column names:")
    print(df.columns.tolist())
    print()
    print("Data types:")
    print(df.dtypes)


def check_cpi_quality(df):
    """Run data quality checks on the CPI dataset."""
    print("=== CPI Data Quality Checks ===")
    print()

    print("Missing Values:")
    print(df.isnull().sum())
    print()

    missing_cpi = df[df["CPIAUCSL"].isnull()]
    print("Rows with missing CPI values:")
    print(missing_cpi)
    print()

    print("Duplicate Rows:")
    print(df.duplicated().sum())
    print()

    print("Duplicate Dates:")
    print(df["observation_date"].duplicated().sum())
    print()

    dates = pd.to_datetime(df["observation_date"], errors="coerce")

    print("Invalid Dates:")
    print(dates.isnull().sum())
    print()

    print("Date Range:")
    print(f"Earliest: {dates.min()}")
    print(f"Latest: {dates.max()}")
    print()

    print("Dates in Chronological Order:")
    print(dates.is_monotonic_increasing)
    print()

    expected_dates = pd.date_range(
        start=dates.min(),
        end=dates.max(),
        freq="MS"
    )

    missing_months = expected_dates.difference(dates)

    print("Missing Months:")
    print(len(missing_months))

    if len(missing_months) > 0:
        print(missing_months)
    print()

    print("Unique Dates:")
    print(dates.nunique())
    print()

    print("CPI Value Range:")
    print(f"Minimum: {df['CPIAUCSL'].min()}")
    print(f"Maximum: {df['CPIAUCSL'].max()}")
    print()

    negative_cpi = (df["CPIAUCSL"] < 0).sum()
    print("Negative CPI Values:")
    print(negative_cpi)


def profile_unemployment(df):
    """Display basic information about the unemployment dataset."""
    print("Unemployment Dataset Profile")
    print("----------------------------")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print()
    print("Column names:")
    print(df.columns.tolist())
    print()
    print("First 5 rows:")
    print(df.head())
    print()
    print("Data types:")
    print(df.dtypes)


def check_unemployment_quality(df):
    """Run data quality checks on the unemployment dataset."""
    print("=== Unemployment Data Quality Checks ===")
    print()

    print("Missing Values:")
    print(df.isnull().sum())
    print()

    print("Duplicate Rows:")
    print(df.duplicated(subset=["year", "period"]).sum())
    print()

    year_month = df["year"].astype(str) + "-" + df["period"].astype(str)

    print("Duplicate Year-Month Observations:")
    print(year_month.duplicated().sum())
    print()

    years = pd.to_numeric(df["year"], errors="coerce")

    print("Invalid Years:")
    print(years.isnull().sum())
    print()

    valid_periods = df["period"].astype(str).str.match(r"^M(0[1-9]|1[0-2])$")

    print("Invalid Month Codes:")
    print((~valid_periods).sum())
    print()

    unemployment_values = pd.to_numeric(df["value"], errors="coerce")

    print("Invalid Unemployment Values:")
    print(unemployment_values.isnull().sum())
    print()

    print("Rows with invalid unemployment values:")
    print(
        df[unemployment_values.isnull()][
            ["year", "period", "periodName", "value"]
        ]
    )
    print()

    print("Unemployment Rate Range:")
    print(f"Minimum: {unemployment_values.min()}")
    print(f"Maximum: {unemployment_values.max()}")
    print()

    print("Negative Unemployment Rates:")
    print((unemployment_values < 0).sum())
    print()

    dates = pd.to_datetime(
        df["year"].astype(str)
        + "-"
        + df["period"].str.replace("M", "", regex=False)
        + "-01",
        errors="coerce"
    )

    print("Invalid Dates:")
    print(dates.isnull().sum())
    print()

    print("Dates in Chronological Order:")
    print(dates.is_monotonic_decreasing)
    print()

    print("Date Range:")
    print(f"Latest: {dates.max()}")
    print(f"Earliest: {dates.min()}")


def profile_mrts(df):
    """Display basic information about the MRTS dataset."""
    print("MRTS Dataset Profile")
    print("---------------------")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print()
    print("Column names:")
    print(df.columns.tolist())
    print()
    print("First 5 rows:")
    print(df.head())
    print()
    print("Data types:")
    print(df.dtypes)


def check_mrts_quality(df):
    """Run data quality checks on the MRTS dataset."""
    print("=== MRTS Data Quality Checks ===")
    print()

    print("Missing Values:")
    print(df.isnull().sum())
    print()

    print("Duplicate Rows:")
    print(df.duplicated().sum())
    print()

    print("Duplicate Observations:")
    print(
        df.duplicated(
            subset=[
                "data_type_code",
                "time_slot_id",
                "seasonally_adj",
                "category_code",
                "time"
            ]
        ).sum()
    )
    print()

    dates = pd.to_datetime(
        df["time"],
        format="%Y-%m",
        errors="coerce"
    )

    print("Invalid Dates:")
    print(dates.isnull().sum())
    print()

    print("Date Range:")
    print(f"Earliest: {dates.min()}")
    print(f"Latest: {dates.max()}")
    print()

    print("Unique Data Type Codes:")
    print(df["data_type_code"].nunique())
    print()

    print("Unique Category Codes:")
    print(df["category_code"].nunique())
    print()

    valid_seasonally_adj = df["seasonally_adj"].isin(["yes", "no"])

    print("Invalid Seasonally Adjusted Values:")
    print((~valid_seasonally_adj).sum())
    print()

    valid_error_data = df["error_data"].isin(["yes", "no"])

    print("Invalid Error Data Values:")
    print((~valid_error_data).sum())
    print()

    # Convert cell values to numeric where possible.
    # Some Census values contain symbols such as "(S)" and are
    # intentionally non-numeric.
    cell_values = pd.to_numeric(
        df["cell_value"],
        errors="coerce"
    )

    non_numeric_mask = cell_values.isnull()

    print("Non-Numeric Cell Values:")
    print(non_numeric_mask.sum())
    print()

    print("Unique Non-Numeric Cell Values:")
    print(df.loc[non_numeric_mask, "cell_value"].value_counts())
    print()

    print("Numeric Cell Values:")
    print(cell_values.notnull().sum())
    print()

    print("Negative Numeric Cell Values:")
    print((cell_values < 0).sum())
    print()

    print("Minimum Numeric Cell Value:")
    print(cell_values.min())
    print()

    print("Maximum Numeric Cell Value:")
    print(cell_values.max())

if __name__ == "__main__":
    cpi_data = load_cpi_data()

    profile_cpi(cpi_data)
    print()

    check_cpi_quality(cpi_data)
    print()

    unemployment_data = load_unemployment_data()

    profile_unemployment(unemployment_data)
    print()

    check_unemployment_quality(unemployment_data)
    print()

    mrts_data = load_mrts_data()

    profile_mrts(mrts_data)
    print()

    check_mrts_quality(mrts_data)
