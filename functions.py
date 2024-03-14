import requests
from load_env import *
def fetch_news():
    url = api_url
    params = {
        "q": "tesla",
        "from": "2024-02-13",
        "sortBy": "publishedAt",
        "apiKey": api_key
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()

        # Print the received data
        articles = data.get("articles", [])

        return articles


    except requests.exceptions.RequestException as e:
        print("Error:", e)

# Call the function to fetch and print news
# fetch_news()
