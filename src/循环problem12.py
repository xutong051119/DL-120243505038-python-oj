n=int(input())
for i in range(0,n):
    m=int(input())
    if m<=1000:
        tax=0
    elif m>1000 and m<=3000:
        tax=m*0.03
    elif m>3000 and m<=5000:
        tax=m*0.04
    else:
        tax=m*0.06
    print(int(tax) if tax.is_integer() else tax)
