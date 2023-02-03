import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a = int(input())

    i = list(map(int,input().split()))
    i.sort()
    print(i[0], i[len(i)-1])