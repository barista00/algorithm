all_score = 0
for i in range(5):
    score = int(input())
    if score < 40:
        score = 40
    all_score += score
print(all_score//5)