su = int(input())
dan = int(input())
if su < 100:
    tmp =(dan * 0.2)
if su >=100:
    tmp =(dan *0.5)
price = su * tmp
print(price)