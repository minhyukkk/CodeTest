import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**8)

n, m = map(int, input().split())
graph = []
visited = [[0] * m for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(n):
    graph.append(list(map(int, input().rstrip())))

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1

    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and graph[nx][ny] == 1:
                visited[nx][ny] += visited[a][b] + 1
                q.append((nx,ny))

bfs(0,0)
print(visited[n-1][m-1])