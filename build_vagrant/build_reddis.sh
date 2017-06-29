# Ensure Redis is installed
wget http://download.redis.io/redis-stable.tar.gz
tar xvzf redis-stable.tar.gz
cd redis-stable
sudo make install

# Redis config files
sudo mkdir /etc/redis
sudo mkdir /var/redis


sudo cp /home/vagrant/redis-stable/utils/redis_init_script /etc/init.d/redis_6379
sudo cp /vagrant/build_vagrant/redis.conf /etc/redis/6379.conf
sudo mkdir /var/redis/6379
sudo update-rc.d redis_6379 defaults
sudo /etc/init.d/redis_6379 start
