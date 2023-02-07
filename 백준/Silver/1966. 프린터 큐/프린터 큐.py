from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))

    idx = deque(list(range(n))) # 현재 인덱스 값 하나씩 idx에 넣어줌
    cnt = 0

    while q:
        if q[0] == max(q): # q의 max값과 현재 값이 같다면
            cnt += 1 # 카운트 중가
            q.popleft() # q에서 빼줌

            pop_idx = idx.popleft() # 현재 인덱스 값을 뺴서
            if pop_idx == m: # m과 비교
                print(cnt)
        else:
            q.append(q.popleft()) # 아니면 뒤로 보냄
            idx.append(idx.popleft()) # 인덱스도 마찬가지