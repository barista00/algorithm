arr = [[0]*100 for _ in range(100)] # 0으로된 리스트100개 x좌표 y좌표 100 X 100
for _ in range(4):
    a, b, c, d = map(int, input().split())
    for i in range(b, d): # 행
        for j in range(a, c): # 열
            arr[i][j] = 1 # i 행에서 a~c-1까지 0을 1로 바꾸기 
lst2 = []
for i in arr:
    lst2.append(sum(i))
print(sum(lst2))