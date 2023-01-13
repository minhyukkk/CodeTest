from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

def bfs():
    dx = [-1, 1, 2, 2, 1, -1, -2, -2]
    dy = [2, 2, 1, -1, -2, -2, -1, 1]

    q = deque()
    q.append((startX, startY))
    while q:
        x,y = q.popleft()
        if x == endX and y == endY:
            return graph[x][y] - 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0<= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))

for i in range(t):
    n = int(input())
    startX, startY = map(int, input().split())
    endX, endY = map(int, input().split())
    graph = [[0]*n for _ in range(n)]
    graph[startX][startY] = 1
    print(bfs())
