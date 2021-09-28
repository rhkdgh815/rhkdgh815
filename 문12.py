g = int(input("구술"))
p = int(input("필기"))
w = int(input("원서"))
t = int(input("토익"))

ave = (g+p+w)/3

if ave >= 80 or t >= 550 :
    print("합격")
else:
    print("불합격")

