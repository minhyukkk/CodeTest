from collections import deque

n = int(input())

graph = [list(map(int,input())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(grpah, x,y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 0
    count = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))
                count += 1
    return count

count = [bfs(graph, i, j) for i in range(n) for j in range(n) if graph[i][j] == 1] # 각 단지마다 입력 해주기 위해서 선언

count.sort()

print(len(count))

for i in range(len(count)):
    print(count[i])