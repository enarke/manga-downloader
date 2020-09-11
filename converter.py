# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 15:25:56 2020

@author: naram
"""
import os
import zipfile
import shutil
from PIL import Image

a=[]
b=[]
for subdir, dirs, files in os.walk(json.load(open('file.json'))["path"]):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file
        if filepath.endswith(".zip"):
            filesize = os.path.getsize(filepath)
            if filesize == 0:
                a.append(filepath.split('\\')[-1].replace(".zip",""))
            else:
                if filepath.endswith(".zip"):
                    try:
                        with zipfile.ZipFile(filepath,"r") as zip_ref:
                            zip_ref.extractall(filepath.replace(".zip",''))
                            zip_ref.close()
                        if os.path.isdir(filepath.replace(".zip",'')):
                            img=[]
                            for subdi, di, fi in os.walk(filepath.replace(".zip",'')):
                                for f in fi:
                                    filp=subdi + os.sep + f
                                    if filp.endswith(".jpg") or filp.endswith(".png"):
                                        im=Image.open(filp)
                                        img.append(im)
                            img[0].save(filepath.replace(".zip",'.pdf'),save_all=True, append_images=img)
                            shutil.rmtree(filepath.replace(".zip",''))
                            os.remove(filepath)
                    except :
                        b.append(filepath.split('\\')[-1].replace(".zip",""))
print("zero size manga chapters",a)
print("corrupted manga chapters",b)
