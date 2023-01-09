from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

graph = [list(input()) for _ in range(n)]
visited =[[0]*n for _ in range(n)]

q = deque()

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    visited[x][y] = 1
    q.append((x,y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == graph[x][y] and visited[nx][ny] == 0: # graph가 같은 색인지 확인해야하니 graph[nx][ny] == graph[x][y] 추가
                visited[nx][ny] = 1
                q.append((nx, ny))

count1 = 0
count2 = 0

#적녹색맹 아닌 경우
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i,j)
            count1 += 1

# 적녹색맹인 경우
visited =[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G': # 색깔 구분 못하니 하나로 통합
            graph[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i,j)
            count2 += 1

print(count1, count2)
