num = input()

li = [int(i) for i in num]
li.sort()

for i in range(1, len(li)+1):
    print(li[-i], end="")