import sys
sys.setrecursionlimit(10**8)

n, m = map(int, input().split())
tree = list(map(int,input().split()))

left, right = 1, max(tree)

while left <= right:
    mid = (left + right) // 2

    sum = 0

    for i in tree:
        if i >= mid:
            sum += i - mid
    
    if sum >= m:
        left = mid +1
    else:
        right = mid - 1
print(right)

# 쉽게 생각하면 저렇게 mid의 값을 정해줌으로서 tree가 움직일 수를 확 줄여버리는 것. -> 라고 생각했으나 left는 1로 해주어야 함
# 그 후 sum과 비교해주면서 m보다 크다면 더 줄일 수 있다!는 거니까 mid의 값을 줄여주고
# m보다 작다면 더 늘릴 수 있는 것이니 하나씩 증가.