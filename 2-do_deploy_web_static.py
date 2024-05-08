#!/usr/bin/python3
# script that deploys my local file to the server
from fabric.api import run, put, env

env.hosts = ['54.237.67.138', '100.25.4.226']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """function to deploy an archive to the servers
    and uncompress it later
    """
    if archive_path is None:
        return False

    try:
        for host in env.hosts:
            path = archive_path.split('/')[-1]
            put(archive_path, '/tmp/')

            run('tar -xzf /tmp/{} -C /data/web_static/releases/'.format(path))
            run('rm /tmp/{}'.format(path))

            real_path = '/data/web_static/releases/{}'.format(path.split('.')[0])
            run('rm -r /data/web_static/current')
            run('sudo ln -s {} /data/web_static/current'.format(real_path))

        return True
    except Exception as e:
        print("error", e)
        return False

