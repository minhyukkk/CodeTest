import sys
import heapq
input = sys.stdin.readline

t = int(input())
heap = []

for _ in range(t):
    num = int(input())

    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-1 * heapq.heappop(heap)) # 바꿨던 값을-1을 곱해 원래의 값으로 다시 되돌림

    else:
        heapq.heappush(heap, (-num)) # 힙은 최소힙이 기본이므로 -1을 해줘 최댓값을 최솟값으로 바꿈