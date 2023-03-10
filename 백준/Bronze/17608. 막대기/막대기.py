import sys
input = sys.stdin.readline

n = int(input())

s = []

for i in range(n):
    h = int(input())
    s.append(h)

count = 1
top = s.pop()

while s:
    su = s.pop()
    if (su > top):
        count += 1
        top = su

print(count)

