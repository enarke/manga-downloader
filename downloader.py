# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 19:39:20 2020

@author: naram
"""
import requests
import os
import threading
import json
def download(manga,start,end):
    path=config["path"]+"\\"+manga[:-1]
    if not os.path.isdir(path):
        os.makedirs(path)
    for i in range(start,end+1):
        i=str(i)
        print(manga,i)
        url = 'http://images.mangafreak.net:8080/downloads/'+manga+i
        # download the file contents in binary format
        r = requests.get(url)
        with open(path+"\\"+manga+i+'.zip', "wb") as zip:
            zip.write(r.content)
        data[manga][0]=int(i)
        print(manga,i,"Done")
    print(manga,"completed")
t=[]
data =json.load(open('file.json'))
config =json.load(open('config.json'))
for i in data.keys():
    if data[i][0]<data[i][1]:
        t.append(threading.Thread(target=download, args=(i,*data[i],)))
for i in t:
    i.start()
for i in t:
    i.join()
print(data)
with open('file.json', 'w') as fp:
    json.dump(data, fp)
