matrix = [list(input()) for _ in range(5)]
for j in range(15):
    for i in matrix:
        try:
            print(i[j], end="")
        except:
            continue