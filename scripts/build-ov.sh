#!/bin/bash

TEMPLATECONF=meta-openvario/conf source oe-init-build-env

# bitbake openvario-image -c listtasks
# bitbake openvario-image -c fetchall
# bitbake openvario-image -g -u depexp

# bitbake -c cleanall openvario-image
bitbake openvario-image

