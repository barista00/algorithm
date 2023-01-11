# 문제 5 입력된값 하나하나씩 더해서 출력
num = input()
a = 0
for i in tuple(num):
    a = a + int(i)
print(a)