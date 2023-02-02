W = []
for i in range(10):
    score = int(input())
    W.append(score)
K = []
for i in range(10):
    score = int(input())
    K.append(score)
W.sort()
K.sort()

W_Top = 0
K_Top = 0
for i in range(1,4):
    W_Top += W[-i]
    K_Top += K[-i]

print(W_Top, K_Top)