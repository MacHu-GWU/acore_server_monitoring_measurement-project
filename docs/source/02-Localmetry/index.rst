Localmetry
==============================================================================
本文将详细介绍如何用这个库来定时采集 worldserver 游戏服务器的性能数据.

**底层实现**

`acore_server_monitoring_measurement/localmetry.py <https://github.com/MacHu-GWU/acore_server_monitoring_measurement-project/blob/main/acore_server_monitoring_measurement/localmetry.py>`_ 模块中的 ``WorldServerStatusMeasurement.measure_on_worldserver_ec2`` 方法实现了对 worldserver 游戏服务器的性能数据进行一次采集.

如果你有需要, 你完全可以将这个方法作为一个库函数在其他项目中使用.

.. dropdown:: acore_server_monitoring_measurement/localmetry.py

    .. literalinclude:: ../../../acore_server_monitoring_measurement/localmetry.py
       :language: python
       :linenos:

**中层封装**

`acore_server_monitoring_measurement/cron_job.py <https://github.com/MacHu-GWU/acore_server_monitoring_measurement-project/blob/main/acore_server_monitoring_measurement/cron_job.py>`_ 实现了两个重要函数:

- :func:`~acore_server_monitoring_measurement.cron_job.run_measure_worldserver_cron_job`: 采集 worldserver 的统计数据并发送到 DynamoDB table 中. 这个 cron job 主要是为了采集一段时间内的历史数据.
- :func:`~acore_server_monitoring_measurement.cron_job.run_log_to_ec2_tag_cron_job`: 采集 worldserver 的统计数据并将其写入到 EC2 AWS Tag. 这个 cron job 主要是为了采集实时数据并给人类看的.

.. important::

    这两个函数只能在 worldserver 所在的 EC2 的环境中运行**, 能自动检测本机的 server_id, 定位到 DynamoDB table 或 EC2 AWS Tag.

.. dropdown:: acore_server_monitoring_measurement/cron_job.py

    .. literalinclude:: ../../../acore_server_monitoring_measurement/cron_job.py
       :language: python
       :linenos:

**采集脚本**

`cron_job/run_log_to_ec2_tag_cron_job.py <https://github.com/MacHu-GWU/acore_server_monitoring_measurement-project/blob/main/cron_job/run_log_to_ec2_tag_cron_job.py>`_ 和 `cron_job/run_measure_worldserver_cron_job.py <https://github.com/MacHu-GWU/acore_server_monitoring_measurement-project/blob/main/cron_job/run_measure_worldserver_cron_job.py>`_ 是用于在 GNU Screen 中后台运行的脚本. 它们会每隔一段时间就采集一次数据. 这两个脚本分别对应中层封装中的两个函数.

**EC2 Init**

最终这个把定时任务放在 GNU Screen session 中运行的动作也要通过随着 EC2 启动时的 cloud-init 脚本来启动. 详细原理请参考 `setup_ec2_run_on_restart_script <https://acore-server-bootstrap.readthedocs.io/en/latest/acore_server_bootstrap/actions/s0_configure_ubuntu/impl.html#acore_server_bootstrap.actions.s0_configure_ubuntu.impl.setup_ec2_run_on_restart_script>`_ 中的文档.
