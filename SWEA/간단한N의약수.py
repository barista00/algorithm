# 입력 수 % range(1, 입력수+1) == 0
num = int(input())
for i in range(1, num+1):
    if num % i == 0:
        print(i, end=" ")