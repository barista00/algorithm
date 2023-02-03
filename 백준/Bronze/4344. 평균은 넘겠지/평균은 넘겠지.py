T = int(input())
for t in range(T):
    scores = list(map(int, input().split()))
    total = 0
    for i in range(1, len(scores)):
        total += scores[i]  

    aver = int(total / scores[0])
    stud = 0
    for i in range(1, len(scores)):
        if scores[i] > aver:
            stud += 1
    result = stud / len(scores[1:len(scores)]) * 100
    print(f'{result:.3f}%')