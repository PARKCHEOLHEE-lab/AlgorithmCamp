cn2 = 1031
cv = 0

for j in range(2, cn2):
    if cn2 % j == 0:
        cv = 1
        break
        
if cv == 1:
    print("%s is Not Prime Number" %(cn2))

else:
    print("%s is Prime Number" %(cn2))