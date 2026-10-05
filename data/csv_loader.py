import csv
from pathlib import Path


def load_csv(filename):
    """Read a CSV file and return a list of dicts (one dict per row)."""
    filepath = Path(__file__).parent / filename
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]