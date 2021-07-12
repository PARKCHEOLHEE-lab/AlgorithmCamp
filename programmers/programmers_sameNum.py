# my code

arr = [1,1,3,3,0,1,1]

def solution(arr):
    answer = []
    answer.append(arr[0])

    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
        
    return answer

print(solution(arr))

# best code

def solution(arr):
    answer = []
    answer.append(arr.pop(0))

    for i in arr:
        if answer[-1] == i: 
            continue
        answer.append(i)

    return answer
    
print(solution(arr))

