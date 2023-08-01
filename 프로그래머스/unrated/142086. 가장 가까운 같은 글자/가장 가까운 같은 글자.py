def solution(s):
    answer = []
    s_index = {}
    
    for i in range(len(s)):
        if s[i] not in s_index: # s_index의 키 값에서 확인
            answer.append(-1)
        else:
            answer.append(i-s_index[s[i]])
        s_index[s[i]] = i
    return answer