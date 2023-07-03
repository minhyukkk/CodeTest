def solution(ingredient):
    answer = 0
    array = []
    
    for i in ingredient:
        array.append(i)
        if array[-4:] == [1,2,3,1]: # array의 마지막 4개가 1,2,3,1이라면?
            answer += 1
            for i in range(4):
                array.pop()
    return answer