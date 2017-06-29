#!/bin/sh
if [ -z "$STY" ]; then exec screen -dm -S screenName /bin/bash "$0"; fi
echo "yolo"