t = int(input())

n_list = []
for _ in range(t):
    n = int(input())
    n_list.append(n)

n_list.sort()

for i in n_list:
    print(i)