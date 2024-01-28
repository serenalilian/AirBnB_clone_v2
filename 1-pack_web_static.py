#!/usr/bin/python3
'''Fabric script to generate .tgz archive'''

from fabric.api import local
from datetime import datetime

def do_pack():
    # Create the versions folder if it doesn't exist
    local("mkdir -p versions")
    
    # Generate the timestamp for the archive name
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    
    # Create the archive path
    archive_path = "versions/web_static_{}.tgz".format(timestamp)
    
    # Create the .tgz archive from the web_static folder
    local("tar -czvf {} web_static".format(archive_path))
    
    # Return the archive path
    return archive_path
