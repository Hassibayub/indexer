# Contents of cli.py
import subprocess
import sys
import os
from finalization.install_with_py import install

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    print('cmd: ', 'streamlit', 'run', os.path.join(dir_path, 'webapp.py'))
    subprocess.call(['streamlit', 'run', os.path.join(dir_path, 'webapp.py')] + sys.argv[1:])
