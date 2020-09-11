# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 17:56:38 2020

@author: naram
"""
import os,json
import requests
a={}
for subdir, dirs, files in os.walk(json.load(open('config.json'))["path"]):
    for file in files:
        filepath = subdir + os.sep + file
        if filepath.endswith(".pdf"):
            if filepath.split('\\')[-2] not in a:
                a[filepath.split('\\')[-2]]=[]
            a[filepath.split('\\')[-2]].append(int(filepath.split('\\')[-1].replace(".pdf","").split('_')[-1]))
            a[filepath.split('\\')[-2]].sort()
b={}
for i in a:
    b[i]=[]
    amax=a[i][-1]
    amin=a[i][0]
    for j in range(amin,amax+1):
        if j not in a[i]:
            b[i].append(j)

path=json.load(open('config.json'))["path"]+"\\"+json.load(open('config.json'))["dummy"]
if not os.path.isdir(path):
    os.mkdir(path)
for i in b:
    for j in b[i]:
        url = 'http://images.mangafreak.net:8080/downloads/'+i+"_"+str(j)
        # download the file contents in binary format
        print(i,j)
        r = requests.get(url)
        print(1,i,j)
        if len(r.content)>1:
            with open(path+"\\"+i+"_"+str(j)+'.zip', "wb") as zip:
                zip.write(r.content)
            print(i,j,"Done")
