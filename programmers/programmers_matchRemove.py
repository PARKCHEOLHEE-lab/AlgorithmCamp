def solution(s):
    stack = []
    for letter in s:
        if len(stack) == 0:
            stack.append(letter)
        else:
            if letter == stack[-1]:
                stack.pop()
            else:
                stack.append(letter)
                
    if len(stack) == 0:
        return 1
    
    return 0

    # return 1 if len(stack) == 0 else 0