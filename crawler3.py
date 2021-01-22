#!/usr/bin/env python
# encoding: utf-8
import os
import re
import requests
import time
from bs4 import BeautifulSoup

###############################################获取系统时间
def GetNowTime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

def getid():
    with open('PMID_PFOS.txt', 'r+', encoding='utf-8-sig') as f:
        id_list = []
        for line in f:
            line = line.strip()
            id_list.append(line)
    f.close()
    return id_list


def geturl(url):
    html = requests.get(url).text
    return html


if __name__ == '__main__':
    num_aticle = 100000
    ID = getid()

    for id in ID:
        num_aticle =num_aticle +1
        if num_aticle % 800 == 0:
            time.sleep(600)
            print(GetNowTime())
        try:
            url = 'https://www.ncbi.nlm.nih.gov/pubmed/?term=%s&report=medline&format=text' % id
            xx = geturl(url)
            file = open('Medline_PFOS.txt', 'a', encoding='utf-8-sig')
            file.write(xx)
            file.write('\n\n')
            file.close()
            print('Succeed to write %s' % url)
            print(GetNowTime())
        except :
            num_aticle = num_aticle + 1
            time.sleep(600)
            print(GetNowTime())


