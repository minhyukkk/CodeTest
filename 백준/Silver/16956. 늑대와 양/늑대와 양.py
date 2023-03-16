import sys
input = sys.stdin.readline

x, y = map(int,input().split())
sign = False

graph = []

for i in range(x):
    graph.append(list(input().rstrip()))

for i in range(x):
    for j in range(y):
        if graph[i][j] == 'W':
            dx = [-1,1,0,0]
            dy = [0,0,-1,1]

            for k in range(4):
                nx = dx[k] + i
                ny = dy[k] + j

                if 0<= nx < x and 0<= ny < y and graph[nx][ny] == 'S':
                    sign = True
                    break

        elif graph[i][j] == 'S':
            continue

        elif graph[i][j] == '.':
            graph[i][j] = 'D'

if sign == True:
    print(0)
else:
    print(1)
    for i in graph:
        print(''.join(i))