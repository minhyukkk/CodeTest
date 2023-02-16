import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

n, m, r = map(int, input().split())

visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]
count = 1

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(value):
    global count
    visited[r] = 1
    graph[value].sort(reverse=True)

    for i in graph[value]:
        if visited[i] == 0:
            count += 1
            visited[i] = count
            dfs(i)

dfs(r)

for i in visited[1:]:
    print(i)

