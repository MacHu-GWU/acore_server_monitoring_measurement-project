Telemetry
==============================================================================
本文将详细介绍如何用这个库来定时采集 EC2 和 RDS 状态的数据.

:meth:`acore_server_monitoring_measurement.telemetry.Ec2RdsStatusMeasurement.measure_on_lambda` 能用 Lambda Function 批量采集多台 server 的状态数据并批量写入到 DynamoDB 中. 你的 Lambda Function 的 Layer 中需要包含本项目. 下面给出了一段示例代码:

.. dropdown:: tests_int/test_telemetry.py

    .. literalinclude:: ../../../tests_int/test_telemetry.py
       :language: python
       :linenos:
