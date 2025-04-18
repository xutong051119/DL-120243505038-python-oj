import math
a=float(input())
b=float(input())
c=float(input())
if b*b-4*a*c>0:
    m=(-b+math.sqrt(b*b-4*a*c))/(2*a)
    n=(-b-math.sqrt(b*b-4*a*c))/(2*a)
    if(m<n):
        print(int(m) if m.is_integer() else m,int(n) if n.is_integer() else n)
    else:
        print(int(n) if n.is_integer() else n,int(m) if m.is_integer() else m)
if b*b-4*a*c==0:
    m=(-b+math.sqrt(b*b-4*a*c))/(2*a)
    print(int(m) if m.is_integer() else m)
if b*b-4*a*c<0:
    print("none")
