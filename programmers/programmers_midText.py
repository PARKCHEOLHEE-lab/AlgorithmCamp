# my code

s = "abcded"

def solution(s):
    ss = len(s)
    iss = int(ss/2)

    if ss % 2 == 1:
        return s[iss]
    else:
        return s[iss-1 : iss+1]

print(solution(s))

# best code

def soultion(s):

    return s[(len(s)-1)//2 : len(s)//2+1]

print(solution(s))
