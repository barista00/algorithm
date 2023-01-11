# 문제 6 입력한 수를 제곱해서 하나하나씩 제곱값 다 출력
a = int(input())
b = 2
for i in range(a+1):
    print(b ** i, end=" ")