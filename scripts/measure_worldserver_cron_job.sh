#!/bin/sh
# content of measure_worldserver_cron_job.sh
# try to run measure worldserver Python script every 30 seconds
while :; do
~/git_repos/acore_server_monitoring_measurement-project/.venv/bin/python ~/git_repos/acore_server_monitoring_measurement-project/measure_worldserver.py
sleep 30
done
