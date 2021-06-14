#!/usr/bin/python3
""" Compressing a fabric file"""

from fabric.api import local, env, put, run
from datetime import datetime
import os.path

env.hosts = ['18.208.222.5', '54.146.253.171']


def do_deploy(archive_path):
    """deploy to web-server"""

    if not os.path.exists(archive_path):
        return False

    try:
        archiveName = archive_path[9:]
        archiveNameWOEx = archive_path[:-4]

        put(archive_path, '/tmp/' + archiveName)
        run("mkdir -p /data/web_static/releases/" + archiveNameWOEx)
        run("tar -xzvf /tmp/ " +  archiveName + " -C " + "/data/web_static/releases/" + archiveNameWOEx + " --strip-components=1")
        run("rm -rf /tmp/" + archiveName)
        run("rm -rf /data/web_static/current")
        run("sudo ln -sf /data/web_static/releases/" +
            archiveNameWOEx + " /data/web_static/current")

        return True
    except:
        return False

def do_pack():
    """ pack up out web_static directory """
    try:
        now = datetime.now()

        tarArchiveName = "web_static_"+ now.strftime("%Y%m%d%H%M%S") + ".tgz"
        tarArchivePath = "versions/" + tarArchiveName

        local("mkdir -p versions")
        local("tar -czvf " + tarArchivePath + " web_static")
        return tarArchivePath
    except:
        return None
