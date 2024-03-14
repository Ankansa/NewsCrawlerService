from celery import Celery
from datetime import datetime
from celery.schedules import crontab
from functions import fetch_news
from db_works import DATABASE
from load_env import *

db_ctrl = DATABASE()

c_app = Celery('tasks', broker= e_msg_broker )

@c_app.task
def my_periodic_task():
    print("Task function running...")
    try:
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
    except Exception as e:
        print("Error:", e)    




c_app.conf.beat_schedule = {
    'run-periodic-task-every-5-seconds': {
        'task': 'c_task.my_periodic_task',
        'schedule': 60.0,
    },
}