import os
import re

def ex_1(text):
    return re.findall("[a-z0-9]+",text,flags=re.IGNORECASE)
