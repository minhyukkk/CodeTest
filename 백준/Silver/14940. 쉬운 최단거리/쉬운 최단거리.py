import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)] # 0과 1을 비교해주기 위해서 초기에 -1로 선언


def bfs(i,j):
    dx, dy = [0,0,-1,1], [-1,1,0,0]
    q = deque()
    q.append((i,j))

    visited[i][j] = 0 # 초기 값이기 때문에 0으로 변경

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 0 # 0이라면 갈 수 없는 곳이기 때문에 0으로 변경

                elif graph[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny)) # 1이라면 현재 값에서 1을 증가해서 넣어주고 q에 넣어줌

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2 and visited[i][j] == -1:
            bfs(i,j) # 초기 값 설정

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()