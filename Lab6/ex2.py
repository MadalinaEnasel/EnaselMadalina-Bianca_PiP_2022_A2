import os
import re

def ex_2(r,text,x):
    return list(filter(lambda el:len(el)==x, re.findall(r,text)))