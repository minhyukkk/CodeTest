# 처음에는 직관적으로 짜는 것밖에 생각x 일단 해보자
# 근데 -1을 반환해주는 때를 모르겠어서 검색
# 다들 이렇게는 풀어보지도 않아서 1차 당황
# 출처 https://ji-gwang.tistory.com/249

t = int(input())

# for i in range(t):
#     m, n, x, y = list(map(int, input().split()))
#     a,b = 1, 1
#     count = 1
    
#     while True:
#         if a == x and b == y:
#             break

#         if a < m:
#             a = a+1
#         else:
#             a = 1
#         if b < n:
#             b = b+1
#         else:
#             b = 1

#         count+=1

#     print(count)

for i in range(t):
    m, n, x, y = list(map(int, input().split()))

    k = x
    flag = 0
    while k <= m*n:
        if (k-x) % m == 0 and (k-y) % n == 0:
            print(k)
            flag = 1
            break
        k += m
    if flag == 0:
        print(-1)