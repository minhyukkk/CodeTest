import sys
input = sys.stdin.readline

n, m = map(int,input().split())
su = list(map(int,input().split()))
for i in range(n-1):
    su[i+1] += su[i] # 배열 자체에 그 값을 매번 더해줌
su = [0] + su # 인덱스 초과를 막기 위해 제일 앞에 [0] 추가

for _ in range(m):
    a,b = map(int,input().split())
    print(su[b]-su[a-1])
