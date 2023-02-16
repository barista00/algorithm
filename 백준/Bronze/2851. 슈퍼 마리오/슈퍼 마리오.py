lst = [int(input()) for _ in range(10)]

plus_lst = [0]
plus = 0
for i in lst:
    plus += i
    plus_lst.append(plus)
    if plus >= 100:
        break

num1 = plus_lst[-1] - 100
num2 = abs(plus_lst[-2] - 100)

if num1 <= num2:
    print(plus_lst[-1])
else:
    print(plus_lst[-2])