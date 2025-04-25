f0=0
f1=1
n=int(input())
for i in range(2,n+1):
    f=f0+f1
    f0=f1
    f1=f
if f%3==0:
    print("yes")
else:
    print("no")
