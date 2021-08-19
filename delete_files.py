from pathlib import Path
import os


DIR_read = './files/read'
read_pathList = [name for name in Path(DIR_read).glob('*.txt')]
for file in read_pathList:
    os.remove(file)

DIR_write = './files/write'
write_pathList = [name for name in Path(DIR_write).glob('*.txt')]
for file in write_pathList:
    os.remove(file)

