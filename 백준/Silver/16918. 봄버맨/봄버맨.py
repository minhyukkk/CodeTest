import sys
input = sys.stdin.readline
from collections import deque

# 처음 폭탄
def bomb_1():
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'O':
                q.append((i, j))

# 폭탄 전부 설치
def bomb_2():
    for i in range(r):
        for j in range(c):
            if graph[i][j] != 'O':
                graph[i][j] = 'O'

# 터지는 자리들
def bombs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        a, b = q.popleft()
        graph[a][b] = "."

        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]

            if 0 <= x < r and 0 <= y < c:
                if graph[x][y] == "O":
                    graph[x][y] = "."

r, c, n = map(int,input().split())
# 1단계 폭탄 설치
graph = [list(map(str, input().strip())) for _ in range(r)]

# 봄버맨은 아무것도 1초동안 아무것도 하지 않음
n -= 1

while n:
    # 폭탄의 위치를 저장할 리스트
    q = deque()

    # 폭탄의 위치 저장
    bomb_1()

    # 3단계: 모든 칸의 폭탄을 설치
    bomb_2()

    n -= 1
    if n == 0:
        break

    # 4단계: 3초전에 설치된 폭탄 폭발
    bombs()
    n -= 1

for i in graph:
    print("".join(i))