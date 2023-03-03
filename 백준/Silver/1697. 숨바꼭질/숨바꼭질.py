from collections import deque

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == m:
            print(grape[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and not grape[nx]:
                grape[nx] = grape[x] + 1
                q.append(nx)

MAX = 100000
grape = [0] * (MAX+1)
n, m = map(int, input().split())

bfs()