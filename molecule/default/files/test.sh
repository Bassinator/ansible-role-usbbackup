#!/bin/bash
set -e

dd if=/dev/zero of=image bs=1M count=1024
mkfs.vfat image
mkdir /mnt/usbbackup
mount -o loop image /mnt/usbbackup
touch /mnt/usbbackup/ttt
