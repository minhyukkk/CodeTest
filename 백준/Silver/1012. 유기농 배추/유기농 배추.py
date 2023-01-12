from collections import deque
import sys 
sys.setrecursionlimit(10**8)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

t = int(input())

def bfs(visited, a, b):
    q = deque()
    q.append((a,b))
    visited[a][b] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] == 1:
                visited[nx][ny] = 0
                q.append((nx,ny))
    return

for i in range(t):
    count = 0
    n, m, r = map(int, input().split())
    visited = [[0]*m for _ in range(n)]

    for j in range(r):
        x,y = map(int, input().split())
        visited[x][y] = 1

    for a in range(n):
        for b in range(m):
            if visited[a][b] == 1:
                bfs(visited, a, b)
                count += 1  
    print(count)

