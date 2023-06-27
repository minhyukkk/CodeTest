def solution(s):
    answer = 0
    c1 = 0
    c2 = 0
    for i in s:
        if c1 == c2:
            answer += 1
            k = i
        if k == i:
            c1 += 1
        else:
            c2 += 1
    return answer