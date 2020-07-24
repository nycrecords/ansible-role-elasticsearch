import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_service_is_running_and_enabled(host):
    elasticsearch = host.service("elasticsearch")

    assert elasticsearch.is_running
    assert elasticsearch.is_enabled


def test_package_is_installed(host):
    elasticsearch = host.package('elasticsearch')

    assert elasticsearch.is_installed
    assert elasticsearch.version.startswith('7')
