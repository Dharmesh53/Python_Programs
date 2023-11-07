from bs4 import BeautifulSoup
import requests

URL = "https://www.imdb.com/list/ls000033724/"
response = requests.get(URL)
html = response.text

soup = BeautifulSoup(html, "html.parser")
boxes = soup.find_all(name="h3", class_="lister-item-header")

headings = []
for box in boxes:
    headings.append(box.select("a"))

titles = []
links = []
for heading in headings:
    for i in heading:
        titles.append(i.getText())
        links.append(i.get("href"))

with open("webseries.url", mode='w') as file:
    i = 1
    for title in titles:
        file.write(f"{i}) {title} --> 'https://www.imdb.com{links[i - 1]}' \n")
        i = i + 1
