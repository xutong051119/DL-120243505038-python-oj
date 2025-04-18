x=float(input())
if x<=4:
    n=50;
elif x>4 and x<=8:
    n=50+(x-4)*20
else:
    n=50+80+(x-8)*30  
print(int(n) if n.is_integer() else n)    
