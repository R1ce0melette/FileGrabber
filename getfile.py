from asyncore import read
import shutil
import os
import traceback
from pathlib import Path


os.system('cmd /c mkdir dump')
dst = "./dump"
for p in Path( '.' ).rglob( '**/VN*/*Grabber/**/*.*' ):
    if 'exe' not in str(p.suffix):
        f = open('listfiles.txt', 'a', encoding='utf-8')
        f.write(str(p) + "\n")
        f.close()
        try:
            shutil.copy(p, dst)
        except:
            traceback.print_exc()
