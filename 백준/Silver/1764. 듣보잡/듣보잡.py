
nod = set()
nob = set()

n, m = map(int, input().split())

for i in range(n):
    nod.add(input())
for i in range(m):
    nob.add(input())

result = sorted(list(nod & nob))

print(len(result))

for i in result:
    print(i)