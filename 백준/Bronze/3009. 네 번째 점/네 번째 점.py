xlst = []
ylst = []
for i in range(3):
    x, y = map(int,input().split())
    xlst.append(x)
    ylst.append(y)
def one(a):
    for i in a:
        if a.count(i) == 1:
            print(i, end=" ")
one(xlst)
one(ylst)