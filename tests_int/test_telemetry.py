# -*- coding: utf-8 -*-

import boto3
import pynamodb_mate.api as pm
from acore_server_monitoring_measurement.telemetry import (
    Ec2RdsStatusMeasurement as Base,
)


class Ec2RdsStatusMeasurement(Base):
    class Meta:
        table_name = "acore_server_monitoring_measurement-dev"
        region = "us-east-1"
        billing_mode = pm.constants.PAY_PER_REQUEST_BILLING_MODE


Ec2RdsStatusMeasurement.create_table(wait=True)
boto_ses = boto3.session.Session(profile_name="bmt_app_dev_us_east_1")
Ec2RdsStatusMeasurement.measure_on_outside(
    server_id_list=["sbx-blue"],
    boto_ses=boto_ses,
)
