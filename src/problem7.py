y=int(input())
x=int(input())
if x==1 or x==3 or x==5 or x==7 or x==8 or x==10 or x==12:
    n=31;
if x==4 or x==6 or x==9 or x==11:
    n=30;
if x==2:
    if y%400==0 or y%4==0 and y%100!=0:
        n=29
    else:
        n=28
print(n)        
