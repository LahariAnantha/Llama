import requests
import csv
import os
from pathlib import Path


RAW_DATA_DIR = Path("data/raw")
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)


CPI_URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL"
CPI_FILE = RAW_DATA_DIR / "cpi.csv"

BLS_URL = "https://api.bls.gov/publicAPI/v2/timeseries/data/LNS14000000"
BLS_FILE = RAW_DATA_DIR / "unemployment.json"

def download_file(url, output_path):
    """Download a file from a URL and save it locally."""
    response = requests.get(url)
    response.raise_for_status()

    with open(output_path, "wb") as file:
        file.write(response.content)

    print(f"Downloaded: {output_path}")





def download_bls_data():
    """Download the BLS civilian unemployment rate data."""

    response = requests.get(BLS_URL)
    response.raise_for_status()

    with open(BLS_FILE, "wb") as file:
        file.write(response.content)

    print(f"Downloaded: {BLS_FILE}")



MRTS_URL = "https://api.census.gov/data/timeseries/eits/mrts"
MRTS_FILE = RAW_DATA_DIR / "mrts.csv"


def download_mrts_data():
    """Download the 2025 Census MRTS dataset."""

    api_key = os.getenv("CENSUS_API_KEY")

    if not api_key:
        raise ValueError("CENSUS_API_KEY environment variable is not set.")

    params = {
        "get": "data_type_code,time_slot_id,seasonally_adj,category_code,cell_value,error_data",
        "time": "2025",
        "key": api_key
    }

    response = requests.get(MRTS_URL, params=params)
    response.raise_for_status()

    data = response.json()

    with open(MRTS_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f"Downloaded: {MRTS_FILE}")



if __name__ == "__main__":
    download_file(CPI_URL, CPI_FILE)
    download_bls_data()
    download_mrts_data()