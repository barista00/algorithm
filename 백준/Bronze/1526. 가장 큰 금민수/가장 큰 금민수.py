N = int(input()) 
N = list(map(str, range(N+1)))
blank = []
for i in ['0','1','2','3','5','6','8','9']:
    for j in N:
        if i in j:
            blank.append(int(j))
N = list(map(int, N))
N = set(N)
blank = set(blank)
minsu_li = list(N - blank)
minsu_li.sort()
print(minsu_li[-1])