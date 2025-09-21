import json
from espn_parser import scrape
import sys, os

try:
    data = scrape()
    if not data or all(len(v) == 0 for v in data.values()):
        raise ValueError("Scraper returned empty data")
    # Write to a temporary file first
    with open("weekly_temp.json", "w") as f:
        json.dump(data, f, indent=2)
    # Replace old JSON only if scraper succeeded
    os.replace("weekly_temp.json", "weekly.json")
    print("weekly.json updated successfully!")
except Exception as e:
    print(f"Scraper failed: {e}")
    sys.exit(1)
