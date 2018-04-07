#! /usr/bin/env python
import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_bash_it_installed(host):
    bash_it = host.file('/root/.bash-it')

    assert bash_it.exists
    assert bash_it.is_directory
