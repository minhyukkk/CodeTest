t = int(input())
for _ in range(t):
    n = int(input())

    def test(n):
        dp = [0] *(101)
        dp[1], dp[2], dp[3] = 1,1,1

        for i in range(4, n+1):
            dp[i] = dp[i-3] + dp[i-2]
        return dp[n]

    print(test(n)) 


