repeat=int(input())
for i in range(0,repeat):
    x=float(input())
    n=int(input())
    a=x**n
    if a.is_integer():
        print(int(a))
    else:
        c='%.2f'%a
        print(c)
        
    
    
