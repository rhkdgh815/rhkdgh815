c = int(input("1. 섭씨" "2.화씨 :"))

if c == 1:
    sub = int(input())
    hwa = (sub * 1.8) +32
    print("섭씨",sub,"는 화씨로",hwa,"입니다.")
else :
    hwa = int(input())
    sub = (hwa -32) / 1.8
    print("섭씨",hwa,"는 화씨로",sub,"입니다.")