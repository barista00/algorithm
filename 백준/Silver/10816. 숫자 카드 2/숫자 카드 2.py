from collections import Counter
N = int(input())
cards = list(map(int, input().split()))

M = int(input())
howmany = list(map(int, input().split()))

cards_count = Counter(cards)

lst = []
for i in howmany:
    if i in cards_count:
        print(cards_count[i], end=" ")
    else:
        print(0, end=" ")