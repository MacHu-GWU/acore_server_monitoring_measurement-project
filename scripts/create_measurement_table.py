# -*- coding: utf-8 -*-

import boto3
import pynamodb_mate.api as pm
from acore_server_monitoring_measurement.telemetry import (
    Ec2RdsStatusMeasurement as Base,
)


# ------------------------------------------------------------------------------
# **Enter your environment name here**
# ------------------------------------------------------------------------------
env_name = "sbx"


# ------------------------------------------------------------------------------
# Don't touch code below
# ------------------------------------------------------------------------------
aws_profile_mapping = {
    "sbx": "bmt_app_dev_us_east_1",
    "tst": "bmt_app_test_us_east_1",
    "prd": "bmt_app_prod_us_east_1",
}
aws_profile = aws_profile_mapping[env_name]
boto_ses = boto3.session.Session(profile_name=aws_profile)


class Ec2RdsStatusMeasurement(Base):
    class Meta:
        table_name = f"wserver_infra-{env_name}-server_monitoring"
        region = "us-east-1"
        billing_mode = pm.constants.PAY_PER_REQUEST_BILLING_MODE


print(f"Create {Ec2RdsStatusMeasurement.Meta.table_name!r} DynamoDB Table ...")
Ec2RdsStatusMeasurement.create_table(wait=True)
print(f"Done, preview at {Ec2RdsStatusMeasurement.get_table_overview_console_url()}")
