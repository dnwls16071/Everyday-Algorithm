import re

def solution(s):
    result = ((len(s) == 4) or (len(s) == 6)) and bool(re.match('^[0-9]*$', s))
    return result