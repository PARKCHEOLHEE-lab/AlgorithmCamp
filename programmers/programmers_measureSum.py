def solution(n):
    answer = 0

    for i in range(1, n+1):
        if n % i == 0:
            answer += i
    return answer
    
print(solution(5))


def solution2(n):
    answer = [i for i in range(1, n+1) if n % i == 0]
    
    return sum(answer)

print(solution2(12))