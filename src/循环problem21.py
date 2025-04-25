x=int(input())
m=0
i=0
while x:
    i=i+1
    if x>m:
        m=x
    x=int(input())    
print(i,m)        
