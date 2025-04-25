x=int(input())
m=0
while x:
    if x%10%2==0:
        m=m+x%10
    x=x//10
print(m)    
