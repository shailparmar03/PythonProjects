"""PENDING"""

import requests
from bs4 import BeautifulSoup
URL = "https://www.flipkart.com/puma-rideal-x-1der-sneakers-men/p/itm7c4a5c143ad9a?pid=SHOGHQ8H5HRHFJ4G&lid=LSTSHOGHQ8H5HRHFJ4GUTC7OK&marketplace=FLIPKART&sattr[]=color&st=color"
response = requests.get(url=URL)
response.raise_for_status()

soup=BeautifulSoup(response.content,"html.parser")
print(soup.prettify())

price = soup.find(class_="_30jeq3 _16Jk6d").get_text()
print(price)
price_tag = price.split("₹")[1]


