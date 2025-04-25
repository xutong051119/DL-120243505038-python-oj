n=int(input())
for i in range(1,n+1):
    m=0
    for j in range(1,i):
        if i%j==0:
            m=m+j
    if m==i:
        print(m,end=" ")
