n=int(input())
i=0
while n>0:
    if n%2!=0:
        n=n-n//2-2
    else:
        n=n-n/2-2
    i=i+1
print(i)
