#!/usr/bin/python3

import os, shutil, subprocess, sys

branch  = 'hardknott'

print('python run-docker.py with Branch ', branch)
print('==========================================')
my_env = os.environ.copy()
if sys.platform.startswith('win'):
    # is win
    cwd = os.getcwd().replace('\\', '/')
else:
    # is linux:
    cwd = os.getcwd()

container = 'openvario/' + branch + ':latest'

print(' Path-Variable is: ', cwd, '!!!!!!!!!!!!!!')

dockerfile = 'scripts/Dockerfile'

# target_dir = '/opt/openvario'
target_dir = '/home/pokyuser'
with_docker_build = True
if sys.platform.startswith('win'):
    # is win, but this is very preliminary
    if with_docker_build:
        myprocess = subprocess.Popen(['docker', 'build', '--file', dockerfile, '-t', container, './'], env = my_env, cwd = cwd, shell = False)
        myprocess.wait()
    # myprocess = subprocess.Popen(['docker', 'run', '-u "pokyuser"' , '--rm', '--mount', 'type=bind,source='+ cwd + ',target=' + target_dir, '-it', container
    # myprocess = subprocess.Popen(['docker', 'run', '--rm', '--mount', 'type=bind,source='+ cwd + ',target=' + target_dir, '-it', container
    myprocess = subprocess.Popen(['docker', 'run', '--rm', '--mount', 'type=bind,source='+ cwd + ',target=' + target_dir, '-it', container
       ], env = my_env, cwd = cwd, shell = False)
else:
    # is linux:
    if with_docker_build:
        myprocess = subprocess.Popen(['docker', 'build', '--file', dockerfile, '-t', container, './'], env = my_env, cwd = cwd, shell = False)
        myprocess.wait()
    myprocess = subprocess.Popen(['docker', 'run', '--rm', '--mount', 'type=bind,source='+ cwd + ',target=' + target_dir, '-it', container
       , '--workdir=' + target_dir], env = my_env, cwd = cwd, shell = False)
myprocess.wait()

print('Finish: run-docker.py')

