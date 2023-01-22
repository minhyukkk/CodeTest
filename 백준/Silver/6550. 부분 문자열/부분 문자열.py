import sys
input = sys.stdin.readline

while 1:
    try:
        s, t = input().split()
    
        value = 0
        flag = 0
        for i in range(len(t)):
            if t[i] == s[value]: # value 값 이용해 인덱스 값을 0부터 하나씩 키워가면서 똑같다면 하나 증가해서 다음 비교
                value += 1

                if value == len(s): # 길이가 같다면 안에 있다는 말
                    flag = 1
                    break

        if flag == 1:
            print('Yes')
        else:
            print('No')

    except:
        break