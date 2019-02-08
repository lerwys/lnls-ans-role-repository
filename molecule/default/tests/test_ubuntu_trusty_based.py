import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('ubuntu_trusty_based')


@pytest.mark.parametrize('repo', [
    'https://epicsdeb.bnl.gov/debian/ jessie/main',
    'http://deb.debian.org/debian/ jessie/main',
    'http://security.debian.org/debian-security/ jessie/updates/main'
])
def test_repos(host, repo):
    cmd = host.run('apt-cache policy | grep http | awk \'{print $2,$3}\' | sort -u')

    assert repo in cmd.stdout
