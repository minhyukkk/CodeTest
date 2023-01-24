from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

n,m = map(int,input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

def bfs(graph,x,y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 0
    count = 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))
                count += 1
    return count

route = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            route.append(bfs(graph, i, j))

if len(route) == 0:
    print(0)
    print(0)
else :
    print(len(route))
    print(max(route))