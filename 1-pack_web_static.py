#!/usr/bin/python3
"""Compress before sending module"""
from datetime import datetime
import os
import tarfile


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    new_folder = "versions/"
    new_file = "web_static_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".tgz"
    if not os.path.exists(new_folder):
        os.mkdir(new_folder)
    with tarfile.open(new_folder + new_file, "w:gz") as tarball:
        print("Packing web_static to " + new_folder + new_file)
        tarball.add("web_static", arcname=os.path.basename("web_static"))
    if not os.path.exists(new_folder + new_file):
        return None
    else:
        return new_folder + new_file
