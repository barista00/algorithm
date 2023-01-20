T = int(input())
for t in range(1, 1+T):
    sen = input().split()
    for i in sen:
        print(i[::-1], end=" ")
    print('')