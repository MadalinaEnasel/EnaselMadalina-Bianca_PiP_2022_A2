import os
import re

def ex_4(path_to_xml,attrs, function):
    result = []
    with open(path_to_xml,"r") as f_d:
        for el in re.findall("<\w+.*?>",f_d.read()):
            if(all([re.search(item[0]+"\s*=\s*\""+item[1] + "\"",el,flags=re.I) for item in attrs.items()])):
                result+=[el]
    return result