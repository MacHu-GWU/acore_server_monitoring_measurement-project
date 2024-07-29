# -*- coding: utf-8 -*-

import pynamodb_mate.api as pm
from acore_server_metadata.api import Server
from ..localmetry import (
    WorldServerStatusMeasurement as Base,
)

server = Server.from_ec2_inside()


class WorldServerStatusMeasurement(Base):
    class Meta:
        table_name = f"wserver_infra-{server.env_name}-server_monitoring"
        region = "us-east-1"
        billing_mode = pm.constants.PAY_PER_REQUEST_BILLING_MODE


def measure_worldserver():
    WorldServerStatusMeasurement.measure_on_worldserver_ec2()
