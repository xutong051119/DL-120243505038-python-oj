x=float(input())
if x<=10:
    n=x*0.1
elif x>10 and x<=20:
    n=10*0.1+(x-10)*0.075
elif x>20 and x<=40:
    n=10*0.1+10*0.075+(x-20)*0.05
elif x>40 and x<=60:
    n=10*0.1+10*0.075+20*0.05+(x-40)*0.03
elif x>60 and x<=100:
    n=10*0.1+10*0.075+20*0.05+20*0.03+(x-60)*0.015
elif x>100:
    n=10*0.1+10*0.075+20*0.05+20*0.03+40*0.015+(x-100)*0.01
print(int(n) if n.is_integer() else n)    
    
