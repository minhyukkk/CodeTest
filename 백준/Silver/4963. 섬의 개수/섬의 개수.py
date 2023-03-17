import sys
input = sys.stdin.readline
from collections import deque

def bfs(a,b):
        graph[a][b] = 0
        q = deque()
        q.append((a,b))
        while q:
            a,b = q.popleft()
            dx = [-1, 1, 0, 0, -1, -1, 1, 1]
            dy = [0, 0, -1, 1, 1, -1, 1, -1]

            for i in range(8):
                nx = dx[i] + a
                ny = dy[i] + b

                if 0<=nx<h and 0<=ny<w and graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    q.append((nx, ny))

while True :
    w, h = map(int, input().split())
    result = 0
    graph = []

    if w == 0 and h == 0:
        break

    for i in range(h):
        graph.append(list(map(int, input().split())))

    
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                result += 1
                bfs(i,j)

    print(result)


    
