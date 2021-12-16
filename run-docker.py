#!/usr/bin/python3

import os, shutil, subprocess, sys

branch  = 'hardknott'

print('python run-docker.py with Branch ', branch)
print('==========================================')
my_env = os.environ.copy()
if sys.platform.startswith('win'):    # is win
    cwd = os.getcwd().replace('\\', '/')
else:                                 # is linux:
    cwd = os.getcwd()

image = 'openvario/' + branch + ':latest'

print(' Path-Variable is: ', cwd, '!!!!!!!!!!!!!!')

dockerfile = 'scripts/Dockerfile'

# test image detection
out = open('docker-out.txt', 'w')
myprocess = subprocess.Popen(['docker', 'image', 'ls', '-q', image], env = my_env, cwd = cwd, stdout = out, shell = False)
myprocess.wait()
out.close()

out = open('docker-out.txt', 'r')
image_id = out.read()
out.close()

print('image: ', image,', image-id = ', image_id, ' --- ', len(image_id))

if len(image_id) > 0:  # with_docker_build:
    myprocess = subprocess.Popen(['docker', 'build', '--file', dockerfile, '-t', image, './'], env = my_env, cwd = cwd, shell = False)
    myprocess.wait()

target_dir = '/opt/openvario'
if sys.platform.startswith('win'):
    # is win, but this is very preliminary
    target_dir = '/home/pokyuser'  # overwrite previous!
    # myprocess = subprocess.Popen(['docker', 'run', '-u "pokyuser"' , '--rm', '--mount', 'type=bind,source='+ cwd + ',target=' + target_dir, '-it', image
    # myprocess = subprocess.Popen(['docker', 'run', '--rm', '--mount', 'type=bind,source='+ cwd + ',target=' + target_dir, '-it', image
    myprocess = subprocess.Popen(['docker', 'run', '--rm', '--mount', 'type=bind,source='+ cwd + ',target=' + target_dir, '-it', image
    , './build-image.py'  ], env = my_env, cwd = cwd, shell = False)
    # , '/opt/openvario/build-image.py'  ], env = my_env, cwd = cwd, shell = False)
else:
    # is linux:
    # target_dir = '/home/pokyuser'
    if with_docker_build:
        myprocess = subprocess.Popen(['docker', 'build', '--file', dockerfile, '-t', image, './'], env = my_env, cwd = cwd, shell = False)
        myprocess.wait()

myprocess = subprocess.Popen(['docker', 'run', '--rm', '--mount', 'type=bind,source='+ cwd + ',target=' + target_dir, '-it', image
       , '--workdir=' + target_dir], env = my_env, cwd = cwd, shell = False)
myprocess.wait()

print('Finish: run-docker.py')

