lst = ['c=','c-','dz=','d-','lj','nj','s=','z=']
N = input()
for i in lst:
    N = N.replace(i,'a') 
print(len(N))