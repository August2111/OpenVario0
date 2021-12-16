#!/bin/bash


umount /dev/mmcblk0p1
umount /dev/mmcblk0p2
# wrong? if [ -f "/dev/mmcblk0p3" ]; then
umount /dev/mmcblk0p3

## IMAGE       = "openVario-image-testing"
## OV_NAME     = "OpenVario-linuxtesting"
## IMAGE       = "openvario-image"
## IMAGE       = "ov"
## OV_NAME     = "OpenVario-linux-$IMAGE-glibc-ipk"

SHORT_MACHINE     = "AM70_2"
DATE              = "21350"
TAG_VERSION       = "3.4.1"

IMAGE_NAME  = "OV-$SHORT_MACHINE-$TAG_VERSION-current.img.gz"

gzip -cd poky/build/$IMAGE_NAME | sudo dd of=/dev/mmcblk0 bs=4M status=progress conv=fdatasync
