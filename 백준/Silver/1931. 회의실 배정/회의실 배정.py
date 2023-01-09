n = int(input())
time = []
for _ in range(n):
    start, end = map(int, input().split())
    time.append([start, end])

time = sorted(time, key = lambda a : (a[1], a[0])) # 람다식 key에 튜플로 여러 인자를 주면 해당 인자의 순서대로 정렬
# -> a[1] : end 기준으로 오름차순(내람차순이라고 생각하면 될듯), 그 후 a[0] 기준으로 오름차순 


end_time = 0
count = 0

# 이미 두번의 정렬을 통해 최선의 시간으로 맞춰짐 그러기 때문에 단순하게 시간 비교를 통해 count값만 프린트해줘도 최대값
for start, end in time:
    if start >= end_time:
        end_time = end
        count += 1

print(count)

