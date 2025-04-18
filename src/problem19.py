h=float(input())
if h<=10:
    m=30
elif h>10 and h<=50:
    m=h*3
else:
    m=2.5*h
print(int(m) if m.is_integer() else m)
