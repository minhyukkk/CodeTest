def solution(a, b, n):
    answer = 0
    
    while (a <= n):
        bottle = n % a
        n = (n // a) * b
        answer += n
        n += bottle
    return answer