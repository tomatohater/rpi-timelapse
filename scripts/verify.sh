#!/bin/bash

if pidof -s motion > /dev/null; then
     echo "Motion process is running: $(date)"> /home/pi/cron.log
else
    echo "Motion process not found: $(date)" >> /home/pi/cron.log
    /usr/bin/motion -c /home/pi/timelapse/conf/motion.conf
fi
