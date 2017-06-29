import requests

def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())

if __name__ == '__main__':
	c = 0
	while (c < 1000):
		count_words_at_url('http://nvie.com')
		c += 1