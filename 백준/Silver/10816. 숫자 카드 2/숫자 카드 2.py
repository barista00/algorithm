import sys
from collections import Counter
N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
howmany = list(map(int, sys.stdin.readline().split()))

cards_count = Counter(cards)

lst = []
for i in howmany:
    if i in cards_count:
        print(cards_count[i], end=" ")
    else:
        print(0, end=" ")