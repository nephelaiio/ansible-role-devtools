import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_command(Command):
    assert Command('git --version').rc == 0
    assert Command('gcc --version').rc == 0
    assert Command('g++ --version').rc == 0
    assert Command('make --version').rc == 0
    assert Command('m4 --version').rc == 0
    assert Command('patch --version').rc == 0
