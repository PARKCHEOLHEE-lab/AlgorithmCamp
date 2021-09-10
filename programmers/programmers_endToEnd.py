def solution(n, words):
    
    turn = 1
    person = 2
    answer = [0,0]
    word_list = [words[0]]
    
    for i in range(1, len(words)):
        curr_word = words[i]
        prev_word = words[i-1]
        
        if curr_word in word_list:
            answer = [person, turn]
            break
            
        if curr_word[0] != prev_word[-1]:
            answer = [person, turn]
            break

        word_list.append(curr_word)
        person += 1
        
        if person > n:
            person = 1
            turn += 1
    
    return answer