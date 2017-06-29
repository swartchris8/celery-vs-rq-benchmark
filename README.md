## RQ setup on Mac

Make sure redis server is running and afterwards follow these steps to setup rq with supervisord:
```bash
pip install supervisor
sudo cp supervisord.conf /usr/local/share/supervisord.conf
sudo supervisord
sudo mkdir -p /usr/local/share/supervisor/conf.d/
sudo cp rq_supervisor_mac.conf /usr/local/share/supervisor/conf.d/rq_supervisor.conf
sudo supervisorctl reread
sudo supervisorctl update
```

## RQ setup on Ubuntu

Follow the steps in the Vagrant file
