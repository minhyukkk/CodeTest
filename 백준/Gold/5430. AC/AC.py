# import sys
# input = sys.stdin.readline
# from collections import deque

# t = int(input())

# for i in range(t):
#     p = input()
#     n = int(input())
#     array = deque(input().rstrip()[1:-1].split(","))
#     result = []

#     flag = 0

#     if n == 0:
#         array = []


#     count = 0
#     for j in p:
#         if j =="R":
#             count+=1

#     for j in p:
#         if count % 2 == 0:
#             if j == 'D':
#                 if len(array) == 0:
#                     flag = 1
#                     break
#                 else:
#                     array.popleft()

#         else:
#             if j == 'R':
#                 array.reverse()
#             elif j == 'D':
#                 if len(array) == 0:
#                     flag = 1
#                     break
#                 else:
#                     array.popleft()
#     if flag == 0:
#         print("["+",".join(array)+"]")
#     else:
#         print("error")


from collections import deque

T = int(input())
for tc in range(T):
    query = input()
    k = int(input())
    # q: 입력받은 배열 양방향 큐에 담기
    q = deque(input()[1:-1].split(','))
    # flag: R(뒤집기)를 한 번만 실행하기 위함
    flag = 0
    
    # TIP! deque는 [''] 의 길이를 0이 아닌 1로 취급하기 때문에 초기화 필요!
    if k == 0:  
        q = []
    
    for c in query:
        if c == 'R':
            flag += 1
        elif c == 'D':
            if len(q) == 0:
                print('error')
                break
            else:
                if flag % 2 == 1:
                    q.pop()
                else:
                    q.popleft()
                        
    else:
        if flag % 2 == 1:
            q.reverse()
        print('[' + ','.join(q) + ']')