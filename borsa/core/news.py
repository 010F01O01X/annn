import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

def get_news(stock):
    query = stock + " hisse"
    url = f"https://www.google.com/search?q={query}&tbm=nws"

    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    news = []

    for item in soup.select("div.dbsr")[:5]:
        title = item.select_one("div.JheGif.nDgy9d")
        if not title:
            continue

        title_text = title.text
        link = item.a["href"]

        sentiment = analyze_sentiment(title_text)

        news.append({
            "title": title_text,
            "link": link,
            "sentiment": sentiment
        })

    return news


def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        return "POZİTİF 📈"
    elif polarity < -0.1:
        return "NEGATİF 📉"
    else:
        return "NÖTR ➖"