import requests
from bs4 import BeautifulSoup

page = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")

soup = BeautifulSoup(page.content, "html.parser")

all_links = []

links = soup.select("a")
print("Liczba linków = ", len(links))
for ahref in links:
    text = ahref.text
    text = text.strip() if text is not None else ""

    href = ahref.get("href")
    href = href.strip() if href is not None else ""
    all_links.append({"href": href, "text": text})

print(all_links)