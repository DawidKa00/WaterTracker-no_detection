import os
import sys


def get_version():
    if getattr(sys, 'frozen', False):
        bundle_dir = sys._MEIPASS
    else:
        bundle_dir = os.path.abspath(".")

    version_file = os.path.join(bundle_dir, "version.txt")

    try:
        with open(version_file, "r") as f:
            return f.read().strip()
    except:
        print("No version file.")
        return None


__version__ = get_version()
