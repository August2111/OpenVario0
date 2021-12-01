#!/usr/bin/python3

import os, shutil, subprocess

remote = 'origin'
branch  = 'hardknott'

print('repo-sync.py with Branch', branch)
my_env = os.environ.copy()

def check_out(_remote, _branch, path, git_url = ''):
        if not os.path.isdir(path + '/.git'):
            os.system('git clone ' + git_url + '  -b ' + _branch + ' ' + path)
            print('Cloned: ', _branch)
        else:
            cmd = ['git', 'fetch', '--all']
            print('git '  + cmd[1]+ ':')
            myprocess = subprocess.Popen(cmd, env = my_env, cwd=path, shell = False)
            myprocess.wait()
    
            cmd = ['git', 'checkout', _remote + '/' + _branch]
            print('git '  + cmd[1]+ ':')
            myprocess = subprocess.Popen(cmd, env = my_env, cwd=path, shell = False)
            myprocess.wait()
    
            cmd = ['git', 'switch', '-c', _branch]
            print('git '  + cmd[1]+ ':')
            myprocess = subprocess.Popen(cmd, env = my_env, cwd=path, shell = False)
            myprocess.wait()
    
            cmd = ['git', 'reset', '--hard', _remote + '/' + _branch]
            print('git '  + cmd[1]+ ':')
            myprocess = subprocess.Popen(cmd, env = my_env, cwd=path, shell = False)
            myprocess.wait()
            print('Checkout: ', _branch)
        print('------------------------------------------------------')

check_out(remote, branch, 'poky', 'git://git.yoctoproject.org/poky')
check_out(remote, branch, 'poky/meta-openembedded', 'git://git.openembedded.org/meta-openembedded')
check_out(remote, branch, 'poky/meta-sunxi', 'git://github.com/linux-sunxi/meta-sunxi')
check_out(remote, branch, 'poky/meta-openvario', 'https://github.com/August2111/meta-openvario')

