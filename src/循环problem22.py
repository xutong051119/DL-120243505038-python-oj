n=int(input())
a=0
for i in range(2,n+1):
    b=1
    for j in range(2,i):
        if i%j==0:
            b=0
            break
    if b==1:
        a=a+1
        print(i,end=" ")
print(end='\n')
print(a)        
