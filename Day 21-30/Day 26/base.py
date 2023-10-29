from bs4 import BeautifulSoup

with open("website.html", encoding='utf-8') as html_file:
    html_doc = html_file.read()

soup = BeautifulSoup(html_doc, "html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
all_anchor = soup.find_all(name='a')

for tag in all_anchor:
    # print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find_all(name="h3", class_="heading")
print(section_heading)

company_url = soup.select_one(selector="p a")
print(company_url)

print(soup.select_one(selector="#name"))

print(soup.select(".heading"))
