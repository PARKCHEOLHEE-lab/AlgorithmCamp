cn1 = 35

if cn1 <= 2:
    print("Please enter a number greater than 3.")
    
else:
    for i in range(2, cn1+1):
        if cn1 == i:
            print("%d is Prime Number" %(cn1))
            
        elif cn1 % i == 0:
            print("%d is Not Prime Number" %(cn1))
            break