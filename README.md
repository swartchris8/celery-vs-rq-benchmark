## RQ setup on Mac

### Redis

1, Make sure redis server is running

### RQ with supervisor

1, Customise supervisord.conf and rq_supervisor_mac.conf
2, Follow these steps to setup rq with supervisord:
```bash
pip install supervisor
sudo cp supervisord.conf /usr/local/share/supervisord.conf
sudo supervisord -c supervisord.conf
sudo mkdir -p /usr/local/share/supervisor/conf.d/
sudo cp rq_supervisor_mac.conf /usr/local/share/supervisor/conf.d/rq_supervisor.conf
sudo supervisorctl -c supervisord.conf reread
sudo supervisorctl -c supervisord.conf update
```

## RQ setup on Ubuntu

Follow the steps in the Vagrant file

## Run RQ test

Start rq workers and place a 1000 requests of counting the number of words at nvie.com:

```bash
python test_queue.py
```

## Monitor rq

Poll rq info every 10 sec to see how the queue is going
```bash
rq info -i 10
```

## Celery setup

Setup RabbitMQ

Setup celery

## Run celery test

Start celery workers and place a 1000 requests of counting the number of words at nvie.com:

```bash
celery -A celery_worker worker --loglevel=info --concurrency=4
python test_celery_queue.py
```

## Monitor celery

```bash
celery flower
```
