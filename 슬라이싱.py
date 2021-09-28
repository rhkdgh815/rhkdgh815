# 슬라이싱

idnumber = "020815-1234567"

print("성별 :" + idnumber[7])
print("연 :" + idnumber[0:2]) # 0~2 직전까지 0,1 번째 자리수 
print("월 :" + idnumber[2:4]) # 2~4 직전까지 2,3 번째 자리수
print("일 :" + idnumber[4:6]) # 4~6 직전까지 4,5 번째 자리수

print("생년월일 : " + idnumber[:6]) # 처음부터 6 직전까지
print("뒤 7 자리 :" + idnumber[7:]) # 7부터 끝까지
print("뒤 7 자리 (뒤에부터) :" + idnumber[])