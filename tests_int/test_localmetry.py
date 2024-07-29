# -*- coding: utf-8 -*-

import pynamodb_mate.api as pm
from acore_server_monitoring_measurement.localmetry import (
    WorldServerStatusMeasurement as Base,
)


class WorldServerStatusMeasurement(Base):
    class Meta:
        table_name = "acore_server_monitoring_measurement-dev"
        region = "us-east-1"
        billing_mode = pm.constants.PAY_PER_REQUEST_BILLING_MODE


WorldServerStatusMeasurement.measure_on_worldserver_ec2()
