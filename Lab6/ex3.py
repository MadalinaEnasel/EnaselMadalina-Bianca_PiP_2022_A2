import os
import re

def ex_3(text_chars,list_of_re):
    return [el for el in text_chars if any([re.search(r,el) for r in list_of_re])]
