import sys
input = sys.stdin.readline
from collections import deque

def bfs(i,j):
    q = deque()
    q.append((i,j))
    temp =[]
    temp.append((i,j))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if l <= abs(graph[nx][ny]-graph[x][y]) <= r:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    temp.append((nx,ny))
    return temp

n,l,r = map(int,input().split())
graph = []
for i in range(n):
        graph.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

count = 0

while True:
    visited = [[0]*n for i in range(n)]
    isTrue = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                temp = bfs(i,j)
                if len(temp) > 1:
                    isTrue = True
                    num = sum(graph[x][y] for x,y in temp) // len(temp)
                    for x,y in temp:
                        graph[x][y] = num
    if not isTrue:
        break
    count += 1
print(count)