#import sys
#input = sys.stdin.readline
#sys.setrecursionlimit(10**8)

n = int(input())

def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibonacci(n):
    count2 = 0
    dp = [0] * (n+1)
    dp[2], dp[1] = 1,1
    for i in range(3, n+1):
        count2 += 1
        dp[i] = dp[i-1] + dp[i-2]
    return count2

print(fib(n), fibonacci(n))