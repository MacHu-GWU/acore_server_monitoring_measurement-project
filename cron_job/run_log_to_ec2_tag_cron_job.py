#!/usr/bin/env /home/ubuntu/git_repos/acore_server_monitoring_measurement-project/.venv/bin/python
# -*- coding: utf-8 -*-

"""
Run this script in GNU screen session when EC2 instance is started, it will
measure worldserver status every 1 minutes and write the result to EC2 AWS tags.

You can run the following command to test it in worldserver EC2 instance,
you should see the EC2 AWS tags got updated every 1 minutes::

    /home/ubuntu/git_repos/acore_server_monitoring_measurement/.venv/bin/python /home/ubuntu/git_repos/acore_server_monitoring_measurement-project/cron_job/run_log_to_ec2_tag_cron_job.py
"""

from acore_server_monitoring_measurement.cron_job import run_log_to_ec2_tag_cron_job

run_log_to_ec2_tag_cron_job()
