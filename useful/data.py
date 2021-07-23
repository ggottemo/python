import os, sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
 
root = os.path.split(__file__)[0]
images = os.path.join(root, 'favicon.ico')