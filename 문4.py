n = int(input())
hun = n // 100
n = n - hun*100
ten = n //10
n = n - ten*10
one = n
tot = hun + ten + one