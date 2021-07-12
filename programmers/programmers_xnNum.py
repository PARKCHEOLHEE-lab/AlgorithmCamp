# my code

x = -4
n = 2

def solution(x, n):
    answer = [x*i for i in range(1, n+1)]
    return answer

print(solution(x, n))

# best code

def number_generator(x, n):
    return [i * x + x for i in range(n)]

print(number_generator(2, 5))