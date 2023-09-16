import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
broken = list(map(int, input().split()))

min_count = abs(100-n) # 일단 +-로 이동하는 거리 계산

for i in range(1000001):
    i = str(i)

    for j in range(len(i)): # 자리수 하나씩 비교. 그래서 str로 변환
        if int(i[j]) in broken:
            break # 자리 하나씩 비교하는데 broken에 있으면 break

        elif j == len(i) -1: # 예를 들어 n이 4자리 수라면 그거랑 비교해서
            min_count = min(min_count, abs(int(i) - n) + len(i)) # 최소값 비교

print(min_count)