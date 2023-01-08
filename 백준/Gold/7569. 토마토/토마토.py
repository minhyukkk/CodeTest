from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

m, n, h = map(int,input().split())

graph = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
count = 0
q = deque([])

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append([i,j,k])

def bfs():
    while q:
        z, x, y = q.popleft()
 
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and graph[nz][nx][ny] == 0:
                graph[nz][nx][ny]  = graph[z][x][y] + 1
                q.append([nz,nx, ny])

bfs()

for i in graph:
    for j in i :
        for k in j :
            if k == 0:
                print(-1)
                exit(0)

        count = max(count, max(j))
if count == 1:
    print(0)
else:
    print(count -1)

