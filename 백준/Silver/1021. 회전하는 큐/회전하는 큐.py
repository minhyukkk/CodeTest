from collections import deque

n,m = map(int,input().split())

data = deque([i for i in range(1,n+1)]) # deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) 이런식으로 큐에 삽입

index = list(map(int,input().split())) #뽑아내려고 하는 수의 위치가 index변수에 순서대로 담아있다.

count = 0

for i in index:
    while 1:
        if data[0] == i:
            data.popleft()
            break
        else:
            if data.index(i) <= len(data)//2: # 현재의 인덱스가 전체의 반보다가 작다면
                data.rotate(-1) # 왼쪽으로 이동
                count += 1
            else:
                data.rotate(1) # 아니라면 오른쪽으로 이동
                count += 1

print(count)