import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]


def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1

    while q:
        su = q.popleft()

        for i in graph[su]:
            if not visited[i]:
                visited[i] = visited[su] + 1
                q.append(i)


for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = []
for i in range(1, n+1):
    visited = [0] * (n+1)
    bfs(i)
    result.append(sum(visited))

print(result.index(min(result))+1)