#! /usr/bin/env python
import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_dein_installed(host):
    dein = host.file('/root/.local/share/dein')

    assert dein.exists
    assert dein.is_directory


def test_fugashi_installed(host):
    fugashi_vim = host.file('/root/.fugashi-vim')

    assert fugashi_vim.exists
    assert fugashi_vim.is_directory


def test_exists_vimrc(host):
    vimrc = host.file('/root/.vimrc')

    assert vimrc.exists
    assert vimrc.is_symlink
    assert host.file('/root/.vimrc').linked_to == '/root/.fugashi-vim/.vimrc'
