T = int(input())
for t in range(1, 1 + T):
    problem = input().split()
    for i in problem[1]:
        print(i*int(problem[0]),end="")
    print('')