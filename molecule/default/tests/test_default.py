import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('pkg', [
    'gnupg',
    'apt-transport-https'
])
def test_default_pkgs(host, pkg):
    package = host.package(pkg)

    assert package.is_installed


@pytest.mark.parametrize('repo', [
    'http://deb.debian.org/debian stretch/main',
    'http://security.debian.org/debian-security stretch/updates/main',
    'https://epicsdeb.bnl.gov/debian stretch/staging/main',
])
def test_repos(host, repo):
    cmd = host.run('apt-cache policy | grep http | awk \'{print $2,$3}\' | sort -u')

    assert repo in cmd.stdout


@pytest.mark.parametrize('pkg', [
    'epics-dev',
])
def test_install_deb(host, pkg):
    cmd = host.run('apt-get install -y %s' % pkg)

    assert cmd.rc == 0

    package = host.package(pkg)

    assert package.is_installed
