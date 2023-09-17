# import sys
# input = sys.stdin.readline
# from collections import deque

# t = int(input())
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# def bfs(x,y):
#     q = deque()
#     q.append((x,y))
    

#     while q:
#         e,r = q.popleft()
#         visited[e][r] = 1

#         for i in range(4):
#             nx = e + dx[i]
#             ny = r + dy[i]

#             if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and visited[nx][ny] == 0:
#                 q.append((nx,ny))
    
# for _ in range(t):
#     n, m, k = list(map(int, input().split()))
#     graph = [[0] * m for _ in range(n)]
#     visited = [[0] * m for _ in range(n)]
#     count = 0

#     for i in range(k):
#         a,b = map(int, input().split())
#         graph[a][b] = 1

#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 1 and visited[i][j] == 0:
#                 bfs(i,j)
#                 count += 1
#     print(count)

import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**8)

t = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 0

    while q:
        e,r = q.popleft()
        

        for i in range(4):
            nx = e + dx[i]
            ny = r + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))
    
for _ in range(t):
    n, m, k = list(map(int, input().split()))
    graph = [[0] * m for _ in range(n)]
    count = 0

    for i in range(k):
        a,b = map(int, input().split())
        graph[a][b] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i,j)
                count += 1
    print(count)
