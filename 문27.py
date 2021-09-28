stu = []

for i in range(1,11) :
    sco = int(input())
    if sco == -1 :
        break

tot = sum (stu)
ave = tot/3
print("3명 학생의 평균은",ave)