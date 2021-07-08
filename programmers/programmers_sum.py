# my code

def solution(a, b):
    if a == b:
        return a
    
    elif a > b:
        num_list = list(range(b, a+1))
        answer = sum(num_list)
        return answer
    
    else:
        num_list = list(range(a, b+1))
        answer = sum(num_list)
        return answer

# best code

def solution(a, b):
    if a > b:
        a , b = b, a

    return sum(range(a, b+1))

print(solution(5, 3))