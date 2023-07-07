from bs4 import BeautifulSoup
import requests
# with open("website.html",encoding='UTF8') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents,'html.parser')
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
#
# print(soup.a)
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading= soup.find(name="h3",class_="heading")
# print(section_heading)
#
# company_url=soup.select_one(selector="p a")
# print(company_url)

response = requests.get(url="https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page,"html.parser")
articles = soup.select(selector="span.titleline>a")
print(articles)

article_texts=[]
article_links=[]
for article_tag in articles:
    article_texts.append(article_tag.getText())
    article_links.append(article_tag.get("href"))

print(article_texts)
print(article_links)

points = [int((point.getText().split())[0]) for point in soup.find_all( name="span",class_="score")]
highest_points = max(points)

index = points.index(highest_points)
print(article_texts[index])
print(article_links[index])
print(points[index])