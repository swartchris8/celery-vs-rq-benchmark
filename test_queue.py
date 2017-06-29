from rq import Queue
from redis import Redis
import time
from somewhere import count_words_at_url
from datetime import datetime


# Tell RQ what Redis connection to use
redis_conn = Redis()
q = Queue("low",connection=redis_conn)  # no args implies the default queue


now = datetime.now()
c = 0
while (c < 1000):
	# Delay execution of count_words_at_url('http://nvie.com')
	job = q.enqueue(count_words_at_url, 'http://nvie.com')
	c += 1

end = datetime.now()
print("{0} finished in {1}".format(c, end-now)) 