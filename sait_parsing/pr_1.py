import json

import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent

url = "https://www.problems.ru/view_by_subject_new.php?parent=79&start=0"

headers = {
    "Accept": "*/*",
    "User-Agent": generate_user_agent()
}

req = requests.get(url, headers=headers)
src = req.text

soup = BeautifulSoup(src, "lxml")
table_example = soup.find_all(class_="problemsmallcaptiontable")
all_products_hrefs = []
for i in table_example:
    all_products_hrefs.append(i.find(class_="componentboxlink"))

problems_dict = {}
for item in all_products_hrefs:
    raw_text = item.text
    item_text = raw_text.split('\n\t\t\t\t\t\t')[1]
    item_href = "https://www.problems.ru" + item.get("href")

    problems_dict[item_text] = item_href

with open("all_categories_dict.json", "w", encoding="utf-8") as file:
    json.dump(problems_dict, file, indent=4, ensure_ascii=False)
