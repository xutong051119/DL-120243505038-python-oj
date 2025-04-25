n=int(input())
if n<10:
    print(n)
else:
    while n>=10:
        s=0
        i=n
        while i:
            s=s+i%10
            i=i//10
        n=s
    print(n)            
        
