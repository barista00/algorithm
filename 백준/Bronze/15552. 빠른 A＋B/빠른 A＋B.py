import sys
T = int(input())
for i in range(1, 1+T):
    a, b = map(int,sys.stdin.readline().rstrip().split())
    print(a+b)