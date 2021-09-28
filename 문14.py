spe = int(input())
wei = int(input())
pow = int(input())

if spe <= 4.5:
    if wei >= 50:
        if pow >= 200:
            print("배영")
if spe <= 6.0:
    if wei >= 80:
        if pow >= 500:
            print("잠염")
if spe <= 5.0:
    if wei >= 70:
        if pow >= 300:
            print("자유형")
