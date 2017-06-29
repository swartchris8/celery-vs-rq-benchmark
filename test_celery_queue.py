from celery_worker import count_words_at_url
from datetime import datetime

now = datetime.now()
c = 0
while (c < 1000):
	# Delay execution of count_words_at_url('http://nvie.com')
	work = print(count_words_at_url.delay('http://nvie.com'))
	c += 1

end = datetime.now()
print("{0} finished in {1}".format(c, end-now)) 