import sys
input = sys.stdin.readline

t = int(input())

bar=[int(input()) for _ in range(t)]
num = 0
dp = [0] * t

if len(bar) <= 2:
    print(sum(bar))
else:
    dp[0] = bar[0]
    dp[1] = bar[0] + bar[1]

    for i in range(2, t):
        dp[i] = max(dp[i-3] + bar[i-1] + bar[i], dp[i-2]+ bar[i])
    print(dp[-1])