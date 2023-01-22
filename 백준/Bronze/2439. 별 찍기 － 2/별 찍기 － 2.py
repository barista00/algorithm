N = int(input())
blank = " "
star = "*"
for i in range(1, 1+N):
    print(blank*(N-i), star*i, sep="")