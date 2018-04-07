#! /usr/bin/env python
import os

# http://testinfra.readthedocs.io/en/latest/modules.html
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_anyenv_installed(host):
    anyenv = host.file('/root/.anyenv/bin/anyenv')

    assert anyenv.exists


def test_rbenv_installed(host):
    rbenv = host.file('/root/.anyenv/envs/rbenv/bin/rbenv')

    assert rbenv.exists


def test_ruby_installed(host):
    assert host.exists('/root/.anyenv/envs/rbenv/shims/ruby')
