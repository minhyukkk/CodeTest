from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

max = 0
for i in range(n):

    for j in range(n):
        if graph[i][j] > max:
            max = graph[i][j]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x,y, value, visited):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1

    while q :
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > value and visited[nx][ny] == 0: # 현재 max 값과 비교해서 큰 곳을 하나씩 찾음 붙어 있으면 영역 1개로 표시하기 때문에 갯수는 상관 x
                visited[nx][ny] = 1
                q.append((nx, ny))
                

result = 0
for i in range(max): #0 ~ graph에서 제일 큰 값 전까지 쭉 돈다
    count = 0
    visited = [[0]*n for _ in range(n)]
    for a in range(n):
        for j in range(n):
            if graph[a][j] > i and visited[a][j] == 0: # 합쳐져 있는 영역은 1개로 보기 때문에  count 1개씩 하는게 맞음
                    bfs(a,j, i, visited)
                    count += 1

    if result < count:
        result = count

print(result)
