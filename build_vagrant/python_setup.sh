#!/usr/bin/env bash

VENV_PATH="/vagrant/venv"

# Delete previously built virtualenv
if [[ -d $VENV_PATH ]]; then
    rm -rf $VENV_PATH
    echo "Removing virtualenv $VENV_PATH"
fi

# Create virtualenv and install necessary packages
echo "Setting up virtualenv $VENV_PATH"
virtualenv --python=python3 --no-site-packages $VENV_PATH
. $VENV_PATH/bin/activate
pip install --upgrade pip
pip install -r /vagrant/build_vagrant/python_requirements.txt

# Add /vagrant/ to virtualenv Python path
sudo cp /vagrant/build_vagrant/vagrant.pth /vagrant/venv/lib/python3.4/site-packages

sudo cp /vagrant/build_vagrant/rq_supervisor.conf /etc/supervisor/conf.d/rq_supervisor.conf
sudo supervisorctl reread
sudo supervisorctl update