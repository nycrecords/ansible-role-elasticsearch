import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_fits_install_dir_exists(host):
    assert host.socket("tcp://127.0.0.1:9200").is_listening
    assert not host.socket("tcp://0.0.0.0:9200").is_listening
