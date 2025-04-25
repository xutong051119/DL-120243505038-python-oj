m=int(input())
n=int(input())
if m>n:
    for i in range(1,n+1):
        if m%i==0 and n%i==0:
            a=i
else:
    for i in range(1,m+1):
        if m%i==0 and n%i==0:
            a=i
print(a)            
        
