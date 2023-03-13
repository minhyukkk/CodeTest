import sys
input = sys.stdin.readline

n, m = map(int,input().split())
graph = list(map(int, input().split()))

for i in range(m):
    how = list(map(int, input().split()))

    if how[0] == 1:
        graph[how[1]-1] = how[2]
        

    elif how[0] == 2:
        for i in range(how[1],how[2]+1):
            if graph[i-1] == 0:
                graph[i-1] = 1

            elif graph[i-1] == 1:
                graph[i-1] = 0

    elif how[0] == 3:
        for i in range(how[1],how[2]+1):
            graph[i-1] = 0

    elif how[0] == 4:
        for i in range(how[1],how[2]+1):
            graph[i-1] = 1

for i in range(n):
    print(graph[i], end= " ")
           

