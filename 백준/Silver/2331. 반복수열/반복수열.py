a, p = map(int, input().split())

num = [a]

while 1:
    tmp = 0
    for s in str(num[-1]):
        tmp += int(s) ** p

    if tmp in num:
        break

    num.append(tmp)

print(num.index(tmp))
