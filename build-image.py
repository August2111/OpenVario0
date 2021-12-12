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

machines = [
  'openvario-7-CH070',
  'openvario-7-PQ070',
  'openvario-7-AM070',
  'openvario-57-lvds',
  'openvario-43-rgb',
  'openvario-7-AM070-DS2',
  'openvario-7-CH070-DS2',
  'openvario-57-ldvs-DS2',
]

my_env['MACHINE'] =  machines[0]

myprocess = subprocess.Popen(['scripts/build-ov.sh'], env = my_env, cwd=cwd, shell = False)
myprocess.wait()

# ========================================================================================================================
# ========================================================================================================================
#
print('Finish!!!!')
