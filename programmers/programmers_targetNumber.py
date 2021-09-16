from itertools import product

def solution(numbers, target):
    combination = [(i,-i) for i in numbers]
    combination = list(product(*combination))
    
    answer = 0
    for case in combination:
        if sum(case) == target:
            answer += 1
            
    return answer

    

def solution(numbers, target):
    result = [0]
    for case in numbers:
        case_list = []
        for temp_num in result:
            case_list.extend([temp_num+case, temp_num-case])
            
        result = case_list
    return result.count(target)