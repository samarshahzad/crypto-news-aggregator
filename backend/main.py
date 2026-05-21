from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from bs4 import BeautifulSoup

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/news")
def get_news():

    url = "https://www.coindesk.com/"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    articles = []

    for item in soup.find_all("a"):

        title = item.get_text(strip=True)
        link = item.get("href")

        if title and link:

            if link.startswith("/"):
                link = "https://www.coindesk.com" + link

            articles.append({
                "title": title,
                "link": link
            })

    unique_articles = []
    seen = set()

    for article in articles:
        if article["title"] not in seen:
            seen.add(article["title"])
            unique_articles.append(article)

    return unique_articles[:50]