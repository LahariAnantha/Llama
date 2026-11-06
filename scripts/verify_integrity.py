import hashlib
from pathlib import Path


RAW_DATA_DIR = Path("data/raw")

CHECKSUM_DIR = Path("data/checksums")

MRTS_FILE = RAW_DATA_DIR / "mrts.csv"

CHECKSUM_DIR.mkdir(parents=True, exist_ok=True)


def calculate_sha256(file_path):
    """Calculate the SHA-256 hash of a file."""
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def verify_file(file_path):
    """Calculate and save the SHA-256 hash for a file."""
    checksum = calculate_sha256(file_path)

    checksum_file = CHECKSUM_DIR / f"{file_path.stem}.sha256"

    with open(checksum_file, "w") as file:
        file.write(checksum)

    print(f"File: {file_path}")
    print(f"SHA-256: {checksum}")
    print(f"Saved checksum: {checksum_file}")
    print()



def check_integrity(file_path):
    """Compare the current SHA-256 hash with the saved checksum."""
    current_checksum = calculate_sha256(file_path)

    checksum_file = CHECKSUM_DIR / f"{file_path.stem}.sha256"

    with open(checksum_file, "r") as file:
        saved_checksum = file.read().strip()

    if current_checksum == saved_checksum:
        print(f"PASS: {file_path} has not changed.")
    else:
        print(f"FAIL: {file_path} has changed.")



if __name__ == "__main__":
    cpi_file = RAW_DATA_DIR / "cpi.csv"
    unemployment_file = RAW_DATA_DIR / "unemployment.json"
    mrts_file = RAW_DATA_DIR / "mrts.csv"

    verify_file(cpi_file)
    verify_file(unemployment_file)
    verify_file(mrts_file)

    print("Integrity check:")
    check_integrity(cpi_file)
    check_integrity(unemployment_file)
    check_integrity(mrts_file)