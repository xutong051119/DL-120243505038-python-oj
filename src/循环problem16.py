n=int(input())
m=0
j=0
for i in range(1,n+1):
    x=int(input())
    if x%2==0:
        m=m+x**3
    if x%2!=0:
        j=j+x**2
print(j,m)        
