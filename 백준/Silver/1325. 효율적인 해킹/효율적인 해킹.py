import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

def bfs(s):
	cnt = 1
	queue = deque([s])
	visit = [0 for _ in range(n+1)]
	visit[s] = 1

	while queue:
		x = queue.popleft()

		for i in graph[x]:
			if not visit[i]:
				visit[i] = 1
				cnt += 1
				queue.append(i)

	return cnt

graph = [[] for _ in range(n+1)]

for _ in range(m):
	a,b = map(int,input().split())
	graph[b].append(a)

maxCnt = 1
result = []

for i in range(1,n+1):
	cnt = bfs(i)
	if cnt > maxCnt:
		maxCnt = cnt
		result.clear()
		result.append(i)
	elif cnt == maxCnt:
		result.append(i)

print(*result) # 이렇게 하면 리스트의 [] 빼고 값만 출력 가능