# 최빈수 구하기
T = int(input())
dict = {}
for t in range(1,1+T):
    a = input()
    scores = list(map(int,input().split()))
    for i in scores:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] = dict[i] + 1
    dict_sort = sorted(dict.items(), key = lambda x : x[1], reverse=True) # 데이터타입 튜플로 바뀐거 생각하고
    print(f'#{t} {dict_sort[0][0]}') 
    dict={}