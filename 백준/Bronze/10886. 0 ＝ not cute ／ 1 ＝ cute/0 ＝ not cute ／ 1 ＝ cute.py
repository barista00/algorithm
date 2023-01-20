T = int(input())
not_cute = 0
cute = 0
for t in range(1,1+T):
    vote = int(input())
    if vote == 1:
        cute += 1
    else:
        not_cute += 1
if not_cute > cute:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")