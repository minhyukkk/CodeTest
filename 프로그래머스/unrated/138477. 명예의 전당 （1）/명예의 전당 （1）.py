def solution(k, score):
    answer = []
    array = []
    
    for i in range(len(score)):
        if (len(array) < k):
            array.append(score[i])
        
        else :
            if min(array) < score[i]:
                array.remove(min(array))
                array.append(score[i])
        answer.append(min(array))
    return answer