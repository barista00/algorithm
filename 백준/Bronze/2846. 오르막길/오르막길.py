N = int(input())
road = list(map(int, input().split()))
# 리스트에 데이터를 i-1, i 두개씩 비교하면서 오르막길인지 확인
max_length = 0
start = 0
end = 0 
for i in range(1,N):
    if road[i] > road[i-1]:

        if start == 0:
            start = road[i-1] # 오르막길일 때 start값 할당함
        
        
        if i == N-1: # 처음부터 끝까지 오르막길일 때 end값 할당
            end = road[i]
            length = end - start
            if max_length < length:
                max_length = length
    
    elif road[i] <= road[i-1]: # 오르막길로 가다가 아닌상황일 때 앞 오르막길의 end값 할당
        if start != 0: # 오르막길이 시작한건지 여부 확인
            end = road[i-1]
            length = end - start # 오르막길이 끝나게 되는경우 오르막길 높이 갱신
            if max_length < length:
                max_length = length
            start = 0
print(max_length)