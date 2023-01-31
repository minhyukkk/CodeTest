import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    s = input()
    sum = 0

    for j in s:
        if j == '(':
            sum += 1
        elif j == ')':
            sum -= 1
        if sum < 0: # ')' 이게 더 많아져 sum값이 -로 넘어가는 순간 갯수가 맞지 않아? VPS가 될 수 없기 때문  
            print('NO')
            break
    
    if sum > 0:
        print('NO')
    elif sum == 0: # 0일때만 이라서 조건 명시 해야 함
        print('YES')