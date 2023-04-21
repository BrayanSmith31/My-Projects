import os
import sys
import datetime
import requests
import pandas as pd
from requests_html import HTML

BASE_DIR = os.path.dirname(__file__)
now = datetime.datetime.now()
year = now.year

def url_to_txt(url, filename="world.html", save = False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        if save:
            with open(f"world_{year}.html", 'w', encoding="utf-8") as f:
                    f.write(html_text)
        return html_text
    return ""


def parse_and_extract(url, name = '2023'):
    html_text = url_to_txt(url)
    r_html = HTML(html = html_text)
    table_class = ".imdb-scroll-table"
    r_table = r_html.find(table_class)

    table_data = []
    header_names = []
    if len(r_table) == 1:
        parsed_table = r_table[0]
        rows = parsed_table.find("tr")
        header_row = rows[0]
        header_cols = header_row.find("th")
        header_names = [x.text for x in header_cols]
        for row in rows[1:]:
            cols = row.find("td")
            row_data = []
            for i,col in enumerate(cols):
                row_data.append(col.text)
            table_data.append(row_data)

    df = pd.DataFrame(table_data, columns = header_names)
    path = os.path.join(BASE_DIR,'Movie_Data')
    os.makedirs(path, exist_ok=True)
    filepath = os.path.join("Movie_Data", f"{name}.csv")
    df.to_csv(filepath, index = False)
    return True

url = "https://www.boxofficemojo.com/year/world/"

def run(start_year=None, years_ago=5):
    if start_year == None:
        now = datetime.datetime.now()
        start_year = now.year
    assert isinstance(start_year, int)
    assert isinstance(years_ago, int)
    assert len(f"{start_year}") == 4
    for i in range(0, years_ago+1):
        url = f"https://www.boxofficemojo.com/year/world/{start_year}/"
        parse_and_extract(url, name=start_year)
        print(f"Finish {start_year}")
        start_year -= 1


if __name__ == "__main__":
    start, count = sys.argv[1], sys.argv[2]
    try:
        start = int(sys.argv[1])
    except:
        start = None
    try:
        count = int(sys.argv[2])
    except:
        count = 1
    run(start_year=start, years_ago=count)


