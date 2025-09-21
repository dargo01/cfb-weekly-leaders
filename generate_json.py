# generate_json.py
from espn_parser import scrape
import json

data = scrape()
with open("weekly.json", "w") as f:
    json.dump(data, f, indent=2)

print("weekly.json generated!")
