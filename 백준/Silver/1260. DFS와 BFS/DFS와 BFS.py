from collections import deque

n, m, v = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]

visited = [0] * (n+1)

for i in range(m):
    a,b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def dfs(v):
    visited[v] = 1
    print(v, end=' ')

    for i in range(n+1) :
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)

visited2 = [0] * (n+1)

def bfs(v):
    q = deque()
    q.append(v)
    visited2[v] = 1
    
    while q:
        x = q.popleft()
        print(x, end = ' ')

        for i in range(n+1):
            if visited2[i] == 0 and graph[x][i] == 1:
                q.append(i)
                visited2[i] = 1
        

dfs(v)
print()
bfs(v)