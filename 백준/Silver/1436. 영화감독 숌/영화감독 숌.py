N = int(input())
lst = []
a = 0
while len(lst) != N:
    a = a + 1
    if '666' in str(a):
        lst.append(a)
print(lst[-1])