x=int(input())
m=0
while x:
    b=1
    for i in range(2,x):
        if x%i==0:
            b=0
            break
    if b==1:
        if x>m:
            m=x
    x=int(input())        
if m==0:
    print("no")
else:
    print(m)
            
