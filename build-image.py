#!/usr/bin/python3

import os, shutil, subprocess, sys

print('### Thats OpenVario ###')
print('#   Do it in Docker   #')
print('#######################')
print('build with github.com/OpenVario')
print('')
#--------------------------------------
my_env = os.environ.copy()
cwd = os.getcwd()


my_env['MACHINE'] =  'openvario-7-CH070'
# my_env['MACHINE'] =  'openvario-57-lvds'
# my_env['MACHINE'] =  'openvario-43-rgb'
# my_env['MACHINE'] =  'openvario-7-AM070-DS2'

myprocess = subprocess.Popen(['build-scripts/build-lua.sh'], env = my_env, cwd=cwd+'/poky', shell = False)
# myprocess = subprocess.Popen(['scripts/build-ov.sh'], env = my_env, cwd=cwd+'/poky', shell = False)
# myprocess = subprocess.Popen(['build-scripts/build-u-boot.sh'], env = my_env, cwd=cwd+'/poky', shell = False)
myprocess.wait()

# ========================================================================================================================
# ========================================================================================================================
#
print('Finish!!!!')
