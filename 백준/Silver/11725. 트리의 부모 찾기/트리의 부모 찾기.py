import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

t = int(input())

graph = [[] for _ in range(t+1)]
visited = [0] * (t+1)

for i in range(t-1):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v):
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = v
            dfs(i)

dfs(1)

for i in range(2,t+1):
    print(visited[i])
