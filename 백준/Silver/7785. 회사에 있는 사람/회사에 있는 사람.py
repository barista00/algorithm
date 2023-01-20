T = int(input())
dict = {}
for t in range(1, 1+T):
    in_out = input().split()
    dict[in_out[0]] = in_out[1] 
lst = []
for i in dict:
    if dict[i] == 'enter':
        i.lower()
        lst.append(i)
lst.sort()
for i in lst[::-1]:
    for j in i:
        j[0].upper()
    print(i)