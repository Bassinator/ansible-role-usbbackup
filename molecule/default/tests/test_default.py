import os
import glob

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_backup_archive(host):
    cmd = host.run("ls -l /mnt/usbbackup/instance_*.tar.gz")
    assert cmd.rc == 0
