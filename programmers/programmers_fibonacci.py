def solution(n):
    
    divider = 1234567
    fibo_list = [0,1]
    count = 0
    i = 1
    
    while count < n-1:
        next_num = fibo_list[i-1] + fibo_list[i]
        fibo_list.append(next_num)
        
        i += 1
        count += 1

    answer = fibo_list[-1] % divider    
        
    return answer