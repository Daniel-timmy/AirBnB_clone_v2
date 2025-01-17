#!/usr/bin/python3
"""Decompresses a folder"""
import datetime
from fabric.api import *
import os


env.hosts = ['34.234.204.132', '34.227.90.53']


def do_pack():
    """function for folder compression"""
    try:
        if not os.path.exists('versions'):
            os.makedirs("versions")

        formatt = "%Y%m%d%H%M%S"
        datte = datetime.now().strftime(formatt)

        file_name = "versions/web_static_{}".format(datte)
        local('tar -czvf {} web_static/'.format(file_name))
        return file_name
    except:
        return None


def do_deploy(archive_path):
    """function for deployment"""
    try:
        if not os.path.exists(archive_path):
            return False
        file_name = archive_path[-29:-4]
        file_n = archive_path[-18:-4]
        put(archive_path, '/tmp/')

        run('sudo mkdir -p /data/web_static/releases/{}/'.format(file_name))

        run('sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(archive_path[-29:], file_name))

        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* /data/web_static/releases/web_static_{}/'.format(
            file_n, file_n))

        run('sudo rm -rf /data/web_static/releases/web_static_{}/web_static'.format(file_n))

        local("sudo rm -rf /tmp/{}".format(archive_path[-29:]))

        run('sudo rm -rf /data/web_static/current')

        run('sudo ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(file_name))
    except:
        return False

    return True


def deploy():
    """creates and distributes an archive to your web servers"""
    val = do_pack()
    if val is None:
        return False
    return do_deploy(val)
