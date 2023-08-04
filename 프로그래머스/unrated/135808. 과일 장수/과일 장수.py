def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    array = []
    
    for i in range(len(score)):
        array.append(score[i])
        if(m == len(array)):
            answer += min(array) * m * 1
            array = []
    return answer