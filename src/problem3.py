x=float(input())
if x<=1000:
    n=0
elif x>1000 and x<=3000:
    n=x*0.03
elif x>3000 and x<=5000:
    n=x*0.04
elif x>5000:
    n=x*0.06
print(int(n) if n.is_integer() else n)   
