card_n, b_j = map(int, input().split())
cards = list(map(int, input().split()))
lst = []
for i in range(card_n-2): # 3장을 이용한 문제기 때문에 뒤에 2장을 순회하지 않는다 -2
    for j in range(i+1, card_n-1): # 여긴 1장 앞에서 출발, 뒤 1장을 순회하지 않는다
        for q in range(j+1, card_n): # 앞에 2장을 순회하지않고 맨 뒤까지 순회한다
            total = cards[i] + cards[j] + cards[q]
            if total <= b_j:
                lst.append(total)
print(max(lst))