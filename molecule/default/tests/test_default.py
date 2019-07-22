import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_command(host):
    assert host.command('git --version').rc == 0
    assert host.command('gcc --version').rc == 0
    assert host.command('g++ --version').rc == 0
    assert host.command('make --version').rc == 0
    assert host.command('m4 --version').rc == 0
    assert host.command('patch --version').rc == 0
