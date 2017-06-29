from celery import Celery
import requests

app = Celery('tasks', broker='amqp://localhost')

@app.task
def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())