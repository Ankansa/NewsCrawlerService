from fastapi import FastAPI
from functions import fetch_news
from datetime import datetime
app = FastAPI()
from db_works import DATABASE

db_ctrl = DATABASE()


@app.get("/")
async def read_root():
    news_data = fetch_news()
    
    for article in news_data:
        title = article.get("title", "")
        description = article.get("description", "")
        published_at_str = article.get("publishedAt", "")
        published_at = datetime.strptime(published_at_str, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M:%S")
        source = article.get("source", {}).get("name", "")
        url = article.get("url", "")
        values = (title, description, published_at, source, url)
        db_ctrl.insert_into_db(values)

    return {"data": news_data}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
