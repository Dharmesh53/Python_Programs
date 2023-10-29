from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
html = response.text

soup = BeautifulSoup(html, "html.parser")

articles = soup.select(".athing")
heading = []
for article_tag in articles:
    heading = article_tag.select(".titleline a")

print(heading.getText())

