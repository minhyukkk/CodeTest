def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    array = []
    
    for i in range(len(score)):
        array.append(score[i])
        if len(array) == m:
            answer += min(array) * m
            array = []
    return answer