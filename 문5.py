cho = int(input())
hour = cho // 3600
cho = cho - (3600*2)
min = cho // 60
cho = cho - (60*2)
sec = cho 

print(cho,"초는",hour,"시간",min,"분",sec,"초 입니다.")
