x = input("하나의 문자를 입력하세요")

if x >= "a" and x<="z":
    print("Alpha Character")
elif x >= "0" and x<="9":
    print("Digit")

else:
        print("Special Character")