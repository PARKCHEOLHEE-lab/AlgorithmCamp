from itertools import product

def solution(word):
    
    vowel = "AEIOU"
    dictionary = []
    
    for repeat in range(1, len(vowel)+1):
        cases = list(product(vowel, repeat=repeat))
        
        for i in range(len(cases)):
            combination = ''.join(cases[i])
            dictionary.append(combination)
    
    answer = sorted(dictionary).index(word)+1
    
    return answer