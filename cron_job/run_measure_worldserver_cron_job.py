#!/usr/bin/env /home/ubuntu/git_repos/acore_server_monitoring_measurement-project/.venv/bin/python
# -*- coding: utf-8 -*-

"""
Run this script in GNU screen session when EC2 instance is started, it will
measure worldserver status every 5 minutes and write the result to DynamoDB.

You can run the following command to test it in worldserver EC2 instance,
you should see one item is created every 5 minutes in DynamoDB table::

    /home/ubuntu/git_repos/acore_server_monitoring_measurement-project/.venv/bin/python /home/ubuntu/git_repos/acore_server_monitoring_measurement-project/cron_job/run_measure_worldserver_cron_job.py
"""

from acore_server_monitoring_measurement.cron_job import run_measure_worldserver_cron_job

run_measure_worldserver_cron_job()
