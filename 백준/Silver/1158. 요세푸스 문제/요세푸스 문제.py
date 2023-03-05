from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int,input().split())

q = deque()
result = []

for i in range(n):
    q.append(i+1)


while q:
    for i in range(k-1):
        q.append(q.popleft())
    
    result.append(q.popleft())

print(str(result).replace('[', '<').replace(']', '>'))