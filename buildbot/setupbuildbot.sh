sudo apt-get install build-essential python3-dev libssl-dev libffi-dev
pip install 'buildbot[bundle]'
pip install buildbot-worker
pip install setuptools-trial
buildbot create-master xt_master
mv xt_master/master.cfg.sample xt_master/master.cfg

buildbot-worker create-worker staging-worker localhost staging-worker pass
buildbot start xt_master
buildbot-worker start staging-worker