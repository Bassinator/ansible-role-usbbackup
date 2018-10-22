# Ansible Role: usbbackup

[![Build Status](https://travis-ci.com/Bassinator/ansible-role-usbbackup.svg?branch=master)](https://travis-ci.com/Bassinator/ansible-role-usbbackup)

Install tigerjython into user home directory

## Requirements

java installed

## Role Variables

Available variables are listed below, along with default values:

    installation_os_user: vagrant
    installation_os_group: vagrant
    usbdrive_unit: media-pi-RETROPIE
    backup_source: '/home/{{installation_os_user }}'
    mount_point: /media/pi/RETROPIE
    excludelist:
      - 'tigerjython/tigerjython2.jar'
      - '.\*'


## Dependencies

None.


## Example Playbook

    - hosts: raspberries
      roles:
         - { role: bassinator.tigerjython, installation_os_user: pi, installation_os_group: pi}

## License

GNU GPLv3

## Author Information
This role was created in 2018 by [Bastian Bukatz](https://bassinator.github.io).
