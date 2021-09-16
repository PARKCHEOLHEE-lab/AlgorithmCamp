def solution(s):
    stack = []
    
    for bracket in s:
        if bracket == "(":
            stack.append(bracket)
        
        elif bracket == ")":
            if not stack:
                return False
            else:
                stack.pop()

    return len(stack) == 0