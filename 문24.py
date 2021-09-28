n1 = int(input())
n2 = int(input())
odd_sum = 0
even_ sum = 0
for i in range(n1+n2+1):
    if i % 2 == 1 :
        odd_sum += i
    else:
        even_sum += i
print("짝수:",even_sum,"홀수:",odd_sum)