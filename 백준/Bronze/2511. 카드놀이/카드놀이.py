A_cards = list(map(int, input().split()))
B_cards = list(map(int, input().split()))

A_score = 0
B_score = 0
for i in range(10):
    if A_cards[i] > B_cards[i]:
        A_score += 3
    elif B_cards[i] > A_cards[i]:
        B_score += 3
    elif A_cards[i] == B_cards[i]:
        A_score += 1
        B_score += 1

print(A_score, B_score)
a = 0
if A_score == B_score:
    for i in reversed(range(10)):
        if A_cards[i] > B_cards[i]:
            print('A')
            a = 1
            break
        elif B_cards[i] > A_cards[i]:
            print('B')
            a = 1
            break
    if a != 1:
        print('D')
elif A_score > B_score:
    print('A')
elif B_score > A_score:
    print('B')