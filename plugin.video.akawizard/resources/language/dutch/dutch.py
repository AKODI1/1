# -*- coding: utf-8 -*-

import sys,base64,os,re

def TEST():
    return

def translate(item):
    first = re.sub("3mTA3","",str(item))
    second = base64.b64decode(str(first)).split("AnJa4gB4")
    third = base64.b64decode(second[1]+second[0]).replace('coded!!!','').replace('!!!twice','')
    return third
