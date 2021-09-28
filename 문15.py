score = int(input("점수를 입력해주세요 "))
n = int(input("속도 경기의 경우 1 기록 경기의 경우에는 2를 입력해주세요:"))

if score > 40 : 
    if n == 1:
    print("갱신된 속도 경기의 기록은 :",score)
    if n == 2:
    print("갱신된 기록 경기의 기록은 :",score)
else : 
    print("기록이 이전기록보다 낮아 갱신 불가능")