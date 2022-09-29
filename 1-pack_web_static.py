#!/usr/bin/python3
"""
Fabric generates a .tgz archive from the contents of the web_static folder
"""
from datetime import datetime
from fabric.api import local
from os.path import isdir
from os import path


def do_pack():
    """Generates tgz ."""
    date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    if isdir("versions") is False:
        local("mkdir versions")
    archive = "versions/web_static_{}.tgz".format(date_time)
    local("tar -cvzf {} web_static".format(archive))
    if path.exists(archive):
        return archive
    else:
        return None
