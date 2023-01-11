# 문제 
# 가위 1 바위 2 보 3 A, B두명이 숫자를 내고 이긴사람출력
T, N = list(map(int,input().split()))
if T - N == -2 or T - N == 1:
    print('A')
else :
    print('B')