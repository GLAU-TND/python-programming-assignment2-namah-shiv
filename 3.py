N=bin(int(input("enter the number")))
a=[]
c=1
for i in range(1,len(N)):
    if(N[i-1]==N[i]):
        c+=1
        a.append(c)
    else:
        c=1
print('binary number is',N)
print('maximum consecutive number is',max(a))
