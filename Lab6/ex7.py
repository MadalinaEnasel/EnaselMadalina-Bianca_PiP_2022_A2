import os
import re

def ex_7(string):
    return re.match(r"[1256]\d\d(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{6}$",string) != None
