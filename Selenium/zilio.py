import requests
from bs4 import BeautifulSoup
zillio_url = 'https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.90380887828481%2C%22east%22%3A-122.25136844042969%2C%22south%22%3A37.64655123544605%2C%22west%22%3A-122.61529055957031%7D%2C%22mapZoom%22%3A11%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A2%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get(url = zillio_url,headers=header)
zillio_web_page= response.text


soup = BeautifulSoup(zillio_web_page,"html.parser")
houses = soup.find(class_='List-c11n-8-85-1__sc-1smrmqp-0 srp__sc-1ieen0c-0 JFapv photo-cards')
print(houses)

prices_elements = houses.find_all(class_="srp__sc-16e8gqd-1 jLQjry")

prices=[price.getText() for price in prices_elements]
print(prices)

link_elements = houses.find_all(class_="")