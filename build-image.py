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

# one only!
machines = ['openvario-7-AM070-DS2']

my_env['TEMPLATECONF'] = 'meta-openvario/conf'
myprocess = subprocess.Popen([
    'ls' , '-l'
], env = my_env, cwd=cwd+'/poky', shell = False)
myprocess.wait()

#myprocess = subprocess.Popen([
#    'TEMPLATECONF=meta-openvario/conf source',
#     'source',
#    './oe-init-build-env' # /home/pokyuser
#], env = my_env, cwd=cwd+'/poky', shell = False)
#myprocess.wait()


for machine in machines:
    print('=== Build OV with machine: ', machine, ' ===')
    my_env['MACHINE'] =  machine

    # myprocess = subprocess.Popen([cwd+'scripts/build-ov.sh', 'xcsoar-maps-alps'], env = my_env, cwd=cwd+'poky, shell = False)
    myprocess = subprocess.Popen([
        'printenv',
    ], env = my_env, cwd=cwd+'/poky', shell = True)
    myprocess.wait()
    print('===============================================')
    print('===============================================')

    myprocess = subprocess.Popen([
        'source',
        'oe-init-build-env',
        'build',
        '&&',
        'bitbake',
        'xcsoar-maps-alps'
    ], env = my_env, cwd=cwd+'/poky', shell = True)
    myprocess.wait()
    print('=== OV with machine: ', machine, ' is ready ===')
    print('===============================================')
    print('===============================================')

# ========================================================================================================================
# ========================================================================================================================
#
print('Finish all machines!!!!')
