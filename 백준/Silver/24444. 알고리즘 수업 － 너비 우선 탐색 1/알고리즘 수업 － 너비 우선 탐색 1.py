from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 1

for _ in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(value):
    global cnt

    q = deque([r])
    visited[r] = 1

    while q:
        value = q.popleft()
        graph[value].sort()
        for g in graph[value]:
            if visited[g] == 0:
                cnt += 1
                visited[g] = cnt
                q.append(g)

bfs(r)

for v in visited[1:]:
    print(v)