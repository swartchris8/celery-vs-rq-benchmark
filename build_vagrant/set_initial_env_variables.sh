#!/usr/bin/env bash
#Replace .profile with .bashrc if required
source ~/.profile
if [ -z "$PROJECT_FOLDER" ]; then # only checks if VAR is set, regardless of its value
    echo export PROJECT_FOLDER="/vagrant" >> ~/.profile
fi
source ~/.profile


