sen = input()
a = 0
for i in sen:
    if a > 9:
        print('')
        print(i,end="")
        a = 1
    else:
        print(i,end="")
        a += 1