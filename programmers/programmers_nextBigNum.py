def solution(n):
    N = bin(n).count("1")
    num = n
    
    while True:
        num += 1
        num_1 = bin(num).count("1")
            
        if N == num_1:
            return int(bin(num), 2)