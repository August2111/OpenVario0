#!/bin/bash

# cd poky
TEMPLATECONF=meta-openvario/conf source oe-init-build-env

bitbake $1

