import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(v):
    visited[v] = 1
    for a in graph[v]:
        if visited[a] == 0:
            dfs(a)
count = 0

for i in range(1, n+1):
    if visited[i] == 0:
        dfs(i)
        count += 1
print(count)