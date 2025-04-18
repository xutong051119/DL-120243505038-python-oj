x=int(input())
if x<0 or x>100:
    print("illegal")
else:
    if x>=90 and x<100:
        print("A")
    elif x>=60 and x<90:
        print("B")
    else:
        print("C")
