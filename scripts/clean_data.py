
import json
import re
from pathlib import Path

import pandas as pd




ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"

PROCESSED.mkdir(parents=True, exist_ok=True)



def report_quality(df, dataset_name):
    print(f"\n{dataset_name.upper()} DATA QUALITY")
    print("Total rows:", len(df))
    print("Missing values:")
    print(df.isna().sum())
    print("Exact duplicates:", df.duplicated().sum())
    print("Duplicate dates:", df["date"].duplicated().sum())



def clean_cpi():
    # Load CPI CSV
    df = pd.read_csv(RAW / "cpi.csv")

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower()

    df = df.rename(columns={
        "observation_date": "date",
        "cpiaucsl": "cpi"
    })

    # Ensure required columns exist
    if not {"date", "cpi"}.issubset(df.columns):
        raise ValueError("CPI dataset missing required columns")

    df = df[["date", "cpi"]].copy()

    # Standardize data types
    df["date"] = pd.to_datetime(
        df["date"], errors="coerce"
    )

    df["cpi"] = pd.to_numeric(
        df["cpi"], errors="coerce"
    )

    # Report initial quality issues
    report_quality(df, "CPI")

    # Remove exact duplicate records
    before = len(df)
    df = df.drop_duplicates()
    print("Exact duplicates removed:", before - len(df))

    # Remove records with missing dates or CPI
    before = len(df)
    df = df.dropna(subset=["date", "cpi"])
    print("Rows removed with missing values:", before - len(df))

    # Validate CPI values
    if (df["cpi"] <= 0).any():
        raise ValueError("Invalid CPI values found")

    # Validate unique dates
    if df["date"].duplicated().any():
        raise ValueError("Conflicting CPI dates found")

    # Sort chronologically
    df = df.sort_values("date").reset_index(drop=True)

    # Save cleaned dataset
    df.to_csv(
        PROCESSED / "cpi_clean.csv",
        index=False
    )

    print("Cleaned CPI rows:", len(df))
    print("Saved cpi_clean.csv")

    return df




def clean_retail():
    # Load Census MRTS CSV
    df = pd.read_csv(
        RAW / "mrts.csv",
        dtype={"category_code": str}
    )

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower()

    required = {
        "data_type_code", "seasonally_adj",
        "category_code", "cell_value",
        "error_data", "time"
    }

    if not required.issubset(df.columns):
        raise ValueError("MRTS dataset missing required columns")

    print("\nRETAIL DATA QUALITY")
    print("Original rows:", len(df))
    print("Data types:", df["data_type_code"].unique())
    print("Categories:", df["category_code"].unique())

    # Filter to monthly retail and food services sales
    # SM = Sales - Monthly (millions of dollars)
    # 44X72 = Retail Trade and Food Services
    # yes = Seasonally adjusted
    # no = Actual estimates, not error statistics
    retail = df[
        (df["data_type_code"] == "SM")
        & (df["category_code"] == "44X72")
        & (df["seasonally_adj"] == "yes")
        & (df["error_data"] == "no")
    ].copy()

    if retail.empty:
        raise ValueError(
            "No matching retail and food services sales "
            "found. Check data_type_code and category_code."
        )

    # Standardize dates
    retail["date"] = pd.to_datetime(
        retail["time"],
        format="%Y-%m",
        errors="coerce"
    )

    # Convert sales to numeric
    retail["sales_millions"] = pd.to_numeric(
        retail["cell_value"],
        errors="coerce"
    )

    # Select relevant columns
    retail = retail[
        ["date", "sales_millions"]
    ]

    # Report missing values and duplicates
    print("Selected rows:", len(retail))
    print("Missing values:")
    print(retail.isna().sum())
    print("Exact duplicates:", retail.duplicated().sum())
    print("Duplicate dates:", retail["date"].duplicated().sum())

    # Remove exact duplicates
    before = len(retail)
    retail = retail.drop_duplicates()
    print("Duplicates removed:", before - len(retail))

    # Remove invalid or missing values
    before = len(retail)
    retail = retail.dropna(
        subset=["date", "sales_millions"]
    )
    print("Missing-value rows removed:", before - len(retail))

    # Validate sales values
    if (retail["sales_millions"] < 0).any():
        raise ValueError("Negative retail sales found")

    if retail["date"].duplicated().any():
        raise ValueError("Conflicting retail dates found")

    # Sort chronologically
    retail = retail.sort_values(
        "date"
    ).reset_index(drop=True)

    # Save cleaned dataset
    retail.to_csv(
        PROCESSED / "retail_clean.csv",
        index=False
    )

    print("Cleaned retail rows:", len(retail))
    print("Saved retail_clean.csv")

    return retail





def clean_unemployment():
    # Load BLS JSON file
    with open(
        RAW / "unemployment.json",
        "r",
        encoding="utf-8"
    ) as f:
        raw_data = json.load(f)

    # Verify API response status
    if raw_data.get("status") != "REQUEST_SUCCEEDED":
        raise ValueError("BLS API request was unsuccessful")

    # Extract unemployment series
    series_list = raw_data["Results"]["series"]

    series = next(
        (
            s for s in series_list
            if s["seriesID"] == "LNS14000000"
        ),
        None
    )

    if series is None:
        raise ValueError(
            "Unemployment series LNS14000000 not found"
        )

    records = []

    # Extract monthly observations
    for observation in series["data"]:
        period = observation["period"]

        # Accept only months M01 through M12
        if not re.fullmatch(
            r"M(0[1-9]|1[0-2])",
            period
        ):
            continue

        year = int(observation["year"])
        month = int(period[1:])

        date = pd.Timestamp(
            year=year,
            month=month,
            day=1
        )

        rate = pd.to_numeric(
            observation["value"],
            errors="coerce"
        )

        records.append({
            "date": date,
            "unemployment_rate": rate
        })

    # Convert records into DataFrame
    unemployment = pd.DataFrame(
        records,
        columns=["date", "unemployment_rate"]
    )

    if unemployment.empty:
        raise ValueError(
            "No monthly unemployment records found"
        )

    # Report initial data quality
    report_quality(unemployment, "Unemployment")

    # Remove exact duplicates
    before = len(unemployment)
    unemployment = unemployment.drop_duplicates()

    print(
        "Exact duplicates removed:",
        before - len(unemployment)
    )

    # Check missing unemployment values
    # Identify missing unemployment observations
    missing = unemployment[
        unemployment["unemployment_rate"].isna()
    ]

    print("\nMissing unemployment observations:")
    print(missing.to_string(index=False))
    print("Number of missing observations:", len(missing))

    # Remove missing unemployment observations
    before = len(unemployment)

    unemployment = unemployment.dropna(
        subset=["unemployment_rate"]
    )

    print(
        "Rows removed due to missing unemployment rates:",
        before - len(unemployment)
    )

    # Validate unemployment rates between 0 and 100
    if not unemployment["unemployment_rate"].between(
        0, 100
    ).all():
        raise ValueError(
            "Invalid unemployment rates found"
        )

    # Check duplicate dates
    if unemployment["date"].duplicated().any():
        raise ValueError(
            "Conflicting unemployment dates found"
        )

    # Sort chronologically
    unemployment = unemployment.sort_values(
        "date"
    ).reset_index(drop=True)

    # Save cleaned dataset
    unemployment.to_csv(
        PROCESSED / "unemployment_clean.csv",
        index=False
    )

    print("Cleaned unemployment rows:", len(unemployment))
    print("Saved unemployment_clean.csv")

    return unemployment



def main():
    print("Starting data cleaning workflow...")

    clean_cpi()
    clean_retail()
    clean_unemployment()

    print("\nAll datasets cleaned successfully!")


if __name__ == "__main__":
    main()
