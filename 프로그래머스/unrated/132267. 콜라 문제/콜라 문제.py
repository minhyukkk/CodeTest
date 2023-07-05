def solution(a, b, n):
    answer = 0
    bottle = 0
    
    while True:
        if n >= a:
            bottle = n % a
            n = n//a * b
            answer += n
            n += bottle
        else:
            break
    return answer