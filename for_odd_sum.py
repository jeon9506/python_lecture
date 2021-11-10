i, odd_sum = 0, 0

# for i in range(501, 1001,2) :
#     # print(i)
#     odd_sum = odd_sum + i

for i in range(501, 1001) :
    if i%2 == 1 :
        odd_sum += i

print(f"500과 1000 사이에 있는 홀수의 합계 : {odd_sum}")

