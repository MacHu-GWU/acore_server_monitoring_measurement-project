How to run integration test in AWS EC2 where you run the worldserver:

SSH to the EC2 instance::

    sshec2 ssh

Delete existing code::

    rm -rf /home/ubuntu/git_repos/acore_server_monitoring_measurement-project

Git clone latest repo::

    git clone https://github.com/MacHu-GWU/acore_server_monitoring_measurement-project /home/ubuntu/git_repos/acore_server_monitoring_measurement-project

Git pull latest changes::

    cd /home/ubuntu/git_repos/acore_server_monitoring_measurement-project && git pull

CD to the repo dir::

    cd /home/ubuntu/git_repos/acore_server_monitoring_measurement-project

Create virtualenv::

    virtualenv /home/ubuntu/git_repos/acore_server_monitoring_measurement-project/.venv

Activate virutalenv::

    source /home/ubuntu/git_repos/acore_server_monitoring_measurement-project/.venv/bin/activate

Pip install core dependencies::

    /home/ubuntu/git_repos/acore_server_monitoring_measurement-project/.venv/bin/pip install -e /home/ubuntu/git_repos/acore_server_monitoring_measurement-project

Pip install test dependencies::

    /home/ubuntu/git_repos/acore_server_monitoring_measurement-project/.venv/bin/pip install -r /home/ubuntu/git_repos/acore_server_monitoring_measurement-project/requirements-test.txt

Run integration test::

    /home/ubuntu/git_repos/acore_server_monitoring_measurement-project/.venv/bin/pytest /home/ubuntu/git_repos/acore_server_monitoring_measurement-project/tests_int -s
