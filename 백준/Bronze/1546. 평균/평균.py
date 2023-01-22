N = int(input())
scores = list(map(int,input().split()))
aver = 0
for score in scores:
    aver += (score/max(scores))*100
print(aver/N)