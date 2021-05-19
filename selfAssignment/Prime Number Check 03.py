cn3 = 103

for i in range(1, cn3):
    for j in range(2, i+1):
        if i == j:              # i와 j의 값이 같아질 때 까지 for문을 반복해라.
            print(i)
            
        elif i % j == 0:        # i / j를 한 나머지가 0면 반복문을 break해라
            break