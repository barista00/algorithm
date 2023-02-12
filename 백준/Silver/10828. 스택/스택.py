import sys
N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    command = sys.stdin.readline().split()
    # 만약 command에 push가 있다면
    if 'push' in command:
        stack.append(int(command[1]))
    
    elif 'pop' in command:
        try:
            print(stack.pop())
        except:
            print(-1)
    
    elif 'size' in command:
        print(len(stack))
    
    elif 'empty' in command:
        if stack:
            print(0)
        else:
            print(1)
    
    elif 'top' in command:
        try:
            print(stack[-1])
        except:
            print(-1)