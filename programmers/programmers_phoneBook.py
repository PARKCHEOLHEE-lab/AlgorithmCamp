def solution(phone_book):
    
    sorted_book = sorted(phone_book)
    
    for i in range(len(sorted_book)-1):
        curr_num = sorted_book[i]
        next_num = sorted_book[i+1]
        
        if curr_num == next_num[:len(curr_num)]:
            return False
        
    return True