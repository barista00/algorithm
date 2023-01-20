N = int(input())
v = list(map(int,input().split()))
look = int(input())
cnt = 0
for i in v:
    if look == i:
        cnt+=1
print(cnt)