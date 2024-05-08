#!/usr/bin/python3
# scrpt that creates an achive file

from fabric.api import local
from datetime import datetime


def do_pack():
    """ creates an archive file for web static
    folder
    """
    try:
        local("mkdir versions")

        time = datetime.now()
        time_str = time.strftime("%Y%m%d%H%M%S")
        file_name = 'versions/web_static_'

        local("tar -czvf {}.{}.tgz web_static".format(filename, time_str))

    except Exception:
        return None
