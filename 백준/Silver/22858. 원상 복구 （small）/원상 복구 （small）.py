n, k = map(int, input().split())
card = list(map(int, input().split()))
rule = list(map(int, input().split()))

for _ in range(k):
    tmp = [0]*n
    for i in range(n):
        tmp[rule[i]-1] = card[i]
    card = tmp
print(*card)