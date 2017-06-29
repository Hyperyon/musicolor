# -*- coding:Utf-8 -*-
import glob
import hashlib

dir_path = "the_path_of_music"
BLOCKSIZE = 65536

def get_sha(path):
    hasher = hashlib.sha1()
    with open(path, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    checksum = hasher.hexdigest()
    print checksum
    return checksum

def get_color(checksum):
    return checksum[:36:6]

item = glob.glob(dir_path+"*.mp3")

with open(dir_path+'db.txt', 'a+') as f:
    for element in item:
        color = get_color(get_sha(element))
        f.write(color+' '+element.split('\\')[-1].split('.mp3')[0]+'\n')

