#!/usr/bin/python3
"""Fabric script to generates a .tgz archive from the
contents of the web_static folder of AirBnB Clone repo, using
the function `do_pack`."""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Compress the contents of web_static"""

    #  create `versions` dir if not exists
    local('mkdir -p versions')

    #  create compressed tgz file
    time_stamp = datetime.now().strftime('%Y%m%d%H%M%S')
    path = 'versions/web_static_' + time_stamp + '.tgz'
    result = local('tar -cvzf {} web_static/'.format(path))
    if result.succeeded:
        return path
    else:
        return None
