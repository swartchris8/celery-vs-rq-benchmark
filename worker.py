import os
import redis
from rq import Worker, Queue, Connection
listen = ['high', 'default', 'low']
redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
conn = redis.from_url(redis_url)
if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
        # c = 0
        # while (c < 5):
        #     # Delay execution of count_words_at_url('http://nvie.com')
        #     job = q.enqueue(count_words_at_url, 'http://nvie.com')
        #     print(job.result)   # => None

        #     # Now, wait a while, until the worker is finished
        #     time.sleep(2)
        #     print(job.result)  # => 889
        #     c += 1
