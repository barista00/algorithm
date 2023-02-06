com = int(input())
# 연결된 컴퓨터 수
connec = int(input())
mat = [[] for _ in range(com+1)] # 인덱싱은 0부터인데 컴퓨터 번호의 시작은 1부터라 이렇게 적음(0번 컴퓨터가 있다고 생각하고 넣은거)

# 연결된 수들의 인접리스트 만들기
for i in range(connec):
    v1, v2 = map(int, input().split())
    mat[v1].append(v2)
    mat[v2].append(v1) # 입력받은 2개의 수가 각각의 인덱스 리스트에 들어가야한다 

virus = [False] * (com+1) # 몇번째 컴퓨터가, 몇개의 컴퓨터가 감염되었는지 알기 위함이므로 컴퓨터 대수보다 많아도 상관없다
wait = [1]
virus[1] = True

while wait:
    infect = wait.pop()
    
    for i in mat[infect]:
        if virus[i] == False:
            virus[i] = True
            wait.append(i)
print(virus.count(True)-1) # 1번 컴퓨터 본인은 카운트하지 않음