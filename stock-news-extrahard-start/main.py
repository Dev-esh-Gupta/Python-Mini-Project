import requests
from twilio.rest import Client

# Twilio related setup
TWILIO_SID = "ACa056ee0729ae9b0a149c46b49834549d"
TWILIO_AUTH_TOKEN = "43bb804ddadb16bae8c0c5347e6e3728"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Alphavantage.co api key stock market api
# newsapi.org
STOCK_END_POINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything?"

STOCK_API_KEY = "K2EFQGFCJ1MV155X"
NEWS_API_KEY = "c45f74b0c3784c79a23346498a1e91b8"

parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "IBM",
    "apikey": "demo"
}


response = requests.get(url= STOCK_END_POINT , params=parameter)
response.raise_for_status()

stock_data = response.json()["Time Series (Daily)"]
stock_data_list = [value for (key,value) in stock_data.items()]

yesterday_close_price = stock_data_list[0]["4. close"]
day_before_yesterday_close_price = stock_data_list[1]["4. close"]

different = abs(float(day_before_yesterday_close_price) - float(yesterday_close_price))
diff_percent = different / float(yesterday_close_price) * 100

if diff_percent > 0.1 :
    news_params = {
        "apiKey" : NEWS_API_KEY,
        "qInTitle" : COMPANY_NAME
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_article = articles[:3]
    formatted_article_list = [f"Headlines : {article['title']}. \nBrief: {article['description']}" for article in three_article]
    print(formatted_article_list)
    # Twilio setup for message sending
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_article_list:
        message = client.messages.create(
            body=article,
            from_='+14432620275',
            to='+916307703807'
        )

        print(message.status)



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

