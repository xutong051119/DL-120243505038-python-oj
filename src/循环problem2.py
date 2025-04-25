num=int(input())
for i in range(2,num):
    n=1
    if num%i==0:
        n=0
        break
print(n)
