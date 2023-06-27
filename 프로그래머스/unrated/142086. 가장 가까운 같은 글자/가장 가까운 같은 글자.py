def solution(s):
    answer = []
    s_index = dict()
    
    for i in range(len(s)):
        if s[i] not in s_index:
            answer.append(-1)
        else:
            answer.append(i-s_index[s[i]])
        s_index[s[i]] = i
    
    return answer