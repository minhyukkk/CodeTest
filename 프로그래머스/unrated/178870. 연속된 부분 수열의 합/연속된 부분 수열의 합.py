def solution(sequence, k):
    answer = []
    sum = 0
    left = 0
    left_p = -1
    
    while True:
        if k > sum:
            left_p += 1
            if left_p >= len(sequence):
                break
            sum += sequence[left_p]
        else:
            sum -= sequence[left]
            if left >= len(sequence):
                break
            left += 1
            
        if sum == k:
            answer.append([left, left_p])
            
    answer.sort(key = lambda x: (x[1]-x[0], x[0]))
        
    return answer[0]