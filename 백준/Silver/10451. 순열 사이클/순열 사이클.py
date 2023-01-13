import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

t = int(input())


def dfs(v):
        visited[v] = 1
        next = graph[v]

        if visited[next] == 0:
            dfs(next)

for i in range(t):
    count = 0
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [0] * (n+1)

    
    for i in range(1, n+1):
        if visited[i] == 0:
            dfs(i)
            count += 1
    print(count)