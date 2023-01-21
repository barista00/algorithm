T = int(input())
for t in range(1, 1+T):
    ox = input()
    cnt = 0 
    plus = 0
    for i in ox:
        if i == 'O':
            cnt += 1
            plus = plus + cnt
        else:
            cnt = 0
    print(plus)