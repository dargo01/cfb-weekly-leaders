# espn_parser.py
import requests
from bs4 import BeautifulSoup

def scrape():
    url = "https://www.espn.com/college-football/weekly"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")

    data = {}
    current_category = None
    current_headers = []

    for tr in soup.find_all("tr"):
        classes = tr.get("class", [])

        if "stathead" in classes:
            current_category = tr.get_text(strip=True)
            data[current_category] = []
            current_headers = []

        elif "colhead" in classes:
            current_headers = [td.get_text(strip=True) for td in tr.find_all("td")]

        elif current_category and tr.find_all("td"):
            values = [td.get_text(strip=True) for td in tr.find_all("td")]
            if current_headers and len(values) == len(current_headers):
                row_dict = dict(zip(current_headers, values))
                data[current_category].append(row_dict)
            else:
                data[current_category].append(values)
    return data
