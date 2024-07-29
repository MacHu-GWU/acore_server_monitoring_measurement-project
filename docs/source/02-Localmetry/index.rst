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

`acore_server_monitoring_measurement/cli/impl.py <https://github.com/MacHu-GWU/acore_server_monitoring_measurement-project/blob/main/acore_server_monitoring_measurement/cli/impl.py>`_ 实现了一个 :func:`~acore_server_monitoring_measurement.cli.impl.measure_worldserver` 函数. **它只能在 worldserver 所在的 EC2 的环境中运行**, 能自动检测本机的 server_id, 定位到 DynamoDB table, 并采集 worldserver 的统计数据.

.. dropdown:: acore_server_monitoring_measurement/cli/impl.py

    .. literalinclude:: ../../../acore_server_monitoring_measurement/cli/impl.py
       :language: python
       :linenos:

**采集脚本**

`scripts/measure_worldserver.py <https://github.com/MacHu-GWU/acore_server_monitoring_measurement-project/blob/main/scripts/measure_worldserver.py>`_ 是一个脚本, 它仅仅是 import 了中层封装, 作为一个可供任何调度程序所使用的采集脚本. 每次运行它就能进行一次采集.

.. dropdown:: scripts/measure_worldserver.py

    .. literalinclude:: ../../../scripts/measure_worldserver.py
       :language: python
       :linenos:

**定时任务**

`scripts/measure_worldserver_cron_job.shy <https://github.com/MacHu-GWU/acore_server_monitoring_measurement-project/blob/main/scripts/measure_worldserver_cron_job.sh>`_ 是一个 shell script 脚本, 它可以被放在 GNU Screen session 中后台运行, 每隔一段时间就运行一次上面的采集脚本.

.. dropdown:: scripts/measure_worldserver_cron_job.sh

    .. literalinclude:: ../../../scripts/measure_worldserver_cron_job.sh
       :language: python
       :linenos:

**EC2 Init**

最终这个把定时任务放在 GNU Screen session 中运行的动作也要通过随着 EC2 启动时的 cloud-init 脚本来启动. 详细原理请参考 `setup_ec2_run_on_restart_script <https://acore-server-bootstrap.readthedocs.io/en/latest/acore_server_bootstrap/actions/s0_configure_ubuntu/impl.html#acore_server_bootstrap.actions.s0_configure_ubuntu.impl.setup_ec2_run_on_restart_script>`_ 中的文档.
