# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 21:48:39 2020

@author: naram
"""
import os,requests,threading,json
a={}
config =json.load(open('config.json'))
for subdir, dirs, files in os.walk(os.getcwd()):
    for file in files:
        filepath = subdir + os.sep + file
        if filepath.endswith(".pdf"):
            if filepath.split('\\')[-2] not in a:
                a[filepath.split('\\')[-2]]=[]
            a[filepath.split('\\')[-2]].append(int(filepath.split('\\')[-1].replace(".pdf","").split('_')[-1]))
            a[filepath.split('\\')[-2]].sort()
def download(i,j):
    path=config["path"]+"\\"+i
    url = 'http://images.mangafreak.net:8080/downloads/'+i+"_"+str(j)
    # download the file contents in binary format
    print(i,j)
    r = requests.get(url)
    print(1,i,j)
    if len(r.content)>1:
        with open(path+"\\"+i+"_"+str(j)+'.zip', "wb") as zip:
            zip.write(r.content)
        print(i,"Done")
t=[]
for i in a:
    t.append(threading.Thread(target=download, args=(i,a[i][-1]+1,)))
for i in t:
    i.start()
for i in t:
    i.join()
