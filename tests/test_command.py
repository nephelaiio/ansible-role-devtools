from testinfra.utils.ansible_runner import AnsibleRunner


testinfra_hosts = \
        AnsibleRunner('.molecule/ansible_inventory').get_hosts('test')


def test_command(Command):
    assert Command('git --version').rc == 0
    assert Command('gcc --version').rc == 0
    assert Command('g++ --version').rc == 0
    assert Command('make --version').rc == 0
    assert Command('m4 --version').rc == 0
    assert Command('patch --version').rc == 0
