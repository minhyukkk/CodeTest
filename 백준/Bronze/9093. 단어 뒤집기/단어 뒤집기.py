t = int(input())

for j in range(t):
    s = input().split()

    for i in s:
        print(i[::-1], end=" ")
    print()