# my code

import re

s = "Pyy"

def solution(s):
    s = s.lower()
    if len(re.findall('p', s)) == len(re.findall('y', s)):
        return True
    else:
        return False


def solution(s):
    s = s.lower()
    p = 0
    y = 0
    for i in s:
        if i == "p":
            p += 1
        elif i == "y":
            y += 1
    
    return p == y


# best code

def solution(s):
    
    return s.lower().count('p') == s.lower().count('y')

print(solution(s))