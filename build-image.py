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


my_env['MACHINE'] =  'openvario-7-AM070-DS2'

myprocess = subprocess.Popen(['/opt/openvario/build-script/build-ov.sh'], env = my_env, cwd=cwd+'/poky', shell = False)
myprocess.wait()


# ========================================================================================================================
# ========================================================================================================================
#
print('Finish!!!!')
