T = int(input())
count = 0
for t in range(T):
    
    N = input()
    
    for i in range(len(N)-1):
        if N[i] == N[i+1]:
            pass
        elif N[i] in N[i+1:]:
            count += 1
            break
print(T-count)