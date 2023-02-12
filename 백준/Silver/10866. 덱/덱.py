import sys
from collections import deque
N = int(sys.stdin.readline())
queue = deque([])

for _ in range(N):
    command = sys.stdin.readline().split()
    # 만약 command에 push가 있다면
    if 'push_front' in command:
        queue.appendleft(int(command[1]))

    elif 'push_back' in command:
        queue.append(int(command[1]))
    
    elif 'pop_front' in command:
        try:
            print(queue.popleft())
        except:
            print(-1)
    
    elif 'pop_back' in command:
        try:
            print(queue.pop())
        except:
            print(-1)
    
    elif 'size' in command:
        print(len(queue))
    
    elif 'empty' in command:
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    
    elif 'front' in command:
        try:
            print(queue[0])
        except:
            print(-1)
    
    elif 'back' in command:
        try:
            print(queue[-1])
        except:
            print(-1)