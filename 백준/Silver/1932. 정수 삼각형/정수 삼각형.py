n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(len(lst[i])):
        if j == 0: # 첫번째 인덱스와 마지막은 최대값을 구할 필요없음
            lst[i][j] = lst[i-1][j] + lst[i][j]
        elif j == i:
            lst[i][j] = lst[i-1][j-1] + lst[i][j] # 현재위치보다 하나위 i-1 위에 위치는 하나 적으니 j-1
        else:
            lst[i][j] = lst[i][j] + max(lst[i-1][j-1], lst[i-1][j])
print(max(lst[n-1]))