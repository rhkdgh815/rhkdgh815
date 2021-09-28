num = int(input())
date = int(input())

if date % 2 == 0 :
    if num % 2 == 0 :
       print ("운행가능")
    else :
        print("운행 불가능")

if date % 2 == 1:
    if num % 2 == 1 :
        print("운행가능")
    else :
        print("운행 불가능")

