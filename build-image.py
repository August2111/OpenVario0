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

if len(sys.argv) > 1:
    if sys.argv[1] == '--all' or sys.argv[1] == '-a':
          machines = [
          'openvario-7-CH070',
          'openvario-7-PQ070',
          # n.d. 'openvario-7-AM070',
          'openvario-57-lvds',
          'openvario-43-rgb',
          'openvario-7-AM070-DS2',
          'openvario-7-CH070-DS2',
          # n.d. 'openvario-57-ldvs-DS2',
        ]
    elif sys.argv[1] == 'AM70':
                machines = ['openvario-7-AM070-DS2']
    elif sys.argv[1] == 'PQ70':
                machines = ['openvario-7-PQ070']
    elif sys.argv[1] == 'TX70':
                machines = ['openvario-7-CH070']
    else:
                machines = [sys.argv[1]]
else:
    # only one!
    machines = ['openvario-7-CH070']

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

    target = 'xcsoar-maps-alps'
    target = 'openvario-image'
    
    myprocess = subprocess.Popen([cwd+'/scripts/build-ov.sh', target ], env = my_env, cwd=cwd+'/poky', shell = False)
    
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
