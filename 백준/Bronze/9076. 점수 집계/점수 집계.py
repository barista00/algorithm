T = int(input())
for _ in range(T):
    scores = list(map(int, input().split()))
    scores.sort()
    scores.pop()
    scores.pop(0)
    if scores[-1] - scores[0] >= 4:
        print('KIN')
    else:
        print(sum(scores))