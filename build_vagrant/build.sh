#!/usr/bin/env bash

# install linux requirements
apt-get --yes install $(cat /vagrant/build_vagrant/linux_requirements.txt)
# ensure github repo is known
# ssh-keyscan -H github.com >> ~/.ssh/known_hosts
# # clone repo
# git clone git@github.com:4thOffice/Snapp_AI.git
# chown -R vagrant /home/vagrant/Snapp_AI
# git --git-dir=Snapp_AI/.git --work-tree=Snapp_AI/ checkout development
