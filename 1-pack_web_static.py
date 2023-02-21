#!/usr/bin/python3
"""Compresses a folder"""
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """function for folder compression"""
    try:
        if not os.path.exists('versions'):
            os.makedirs("versions")

        formatt = "%Y%m%d%H%M%S"
        datte = datetime.now().strftime(formatt)

        file_name = "versions/web_static_{}.tgz".format(datte)
        local('tar -czvf {} web_static/'.format(file_name))
        return file_name
    except:
        return None
