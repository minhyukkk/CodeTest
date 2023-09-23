import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
count = 0

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(value):
    global count
    visited[value] = 1

    for i in graph[value]:
        if visited[i] == 0:
            count += 1
            dfs(i)

dfs(1)

print(count)


