from redis import Redis
from rq.decorators import job
import requests
from datetime import datetime


redis_conn = Redis()
@job('low', connection=redis_conn)
def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())

now = datetime.now()
c = 0
while (c < 1000):
	# Delay execution of count_words_at_url('http://nvie.com')
	work = count_words_at_url.delay('http://nvie.com')
	work.perform()
	c += 1

end = datetime.now()
print("{0} finished in {1}".format(c, end-now)) 