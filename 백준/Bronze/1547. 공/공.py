lst = ['ball','X','X'] # ball position
M = int(input())

for m in range(M):
    x, y = map(int, input().split())
    lst[x-1], lst[y-1] = lst[y-1], lst[x-1]

print(lst.index('ball')+1)