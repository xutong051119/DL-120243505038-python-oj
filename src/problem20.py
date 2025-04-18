x=float(input())
if x<=50:
    n=x*0.15
else:
    n=50*0.15+(x-50)*0.25
print(int(n) if n.is_integer() else n)   
