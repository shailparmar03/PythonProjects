import requests

"""Twilio remaining"""

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "K8I0FBUZB2UYE8DO"
NEWS_API_KEY = "7e6e1cf4b6404de3b1dcb6a17fe91bbd"

stock_params = {
    'function':'TIME_SERIES_DAILY_ADJUSTED',
    'symbol':STOCK,
    'apikey':STOCK_API_KEY,
}
stock_response = requests.get(url=STOCK_ENDPOINT,params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()['Time Series (Daily)']
data_list = [value for (key,value) in stock_data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data['4. close'])
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price  = float(day_before_yesterday_data['4. close'])

print(yesterday_closing_price,day_before_yesterday_closing_price)
difference = abs(yesterday_closing_price-day_before_yesterday_closing_price)
print(difference)

diff_percent = (difference/yesterday_closing_price)*100
print(diff_percent)

if diff_percent > 1:
    news_params={
        "apiKey":NEWS_API_KEY,
        "qInTitle":COMPANY_NAME,
    }
    news_response=requests.get(url=NEWS_ENDPOINT,params=news_params)
    articles = news_response.json()['articles']
    print(articles)

    three_articles = articles[:3]
    print(three_articles)

    formatted_articles = [f'Headline: {article["title"]}\nBried: {article["description"]}' for article in three_articles]
    print(formatted_articles)
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

