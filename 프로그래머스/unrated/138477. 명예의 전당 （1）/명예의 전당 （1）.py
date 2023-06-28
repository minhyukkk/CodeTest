
def solution(k, score):
    answer = []
    array = []
    
    for i in score:
        if len(array) < k:
            array.append(i)
        else :
            if min(array) < i:
                array.remove(min(array))
                array.append(i)
        answer.append(min(array))
    return answer