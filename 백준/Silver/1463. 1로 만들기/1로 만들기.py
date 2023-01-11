n = int(input())
dp = [0]*(n+1)

for i in range(2, n+1): #dp[1]은 위에서 0으로 초기화해줘서 딱히 안해줘도 됨
    dp[i] = dp[i-1] +1 # 뒤에 +1은 횟수!! 먼저 뺀 이유는 어차피 밑에서 min함수 사용해서 더 작은 값으로 변환해줌
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] +1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] +1)

print(dp[n])