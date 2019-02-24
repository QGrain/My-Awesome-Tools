#-*- encoding=utf-8 -*-
import os, sys

count = 1
path = sys.path[0]
fileList = os.listdir(path)

for fl in fileList:
    old_dir = os.path.join(path, fl)
    filename = os.path.splitext(fl)[0]
    filetype = os.path.splitext(fl)[1]
    if (filetype == '.py'):
        continue
    new_dir = os.path.join(path, str(count)+filetype)
    os.rename(old_dir, new_dir)
    count = count + 1

