from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
q = deque()

for i in range(t):
    s = input().split()

    if s[0] == 'push':
        q.append(s[1])

    if s[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())

    if s[0] == 'size':
        print(len(q))

    if s[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)

    if s[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])

    if s[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])
