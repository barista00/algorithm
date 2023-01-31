a = 0
dict = {}
for _ in range(10):
    N = int(input())
    a += N
    if N not in dict:
        dict[N] = 1
    else:
        dict[N] += 1
new_dict = sorted(dict.items(), key=lambda x:x[1])
print(a//10)
print(new_dict[-1][0])