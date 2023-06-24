def solution(s, skip, index):
    answer = ''
    skip = set(ord(w) for w in skip)
    for word in s:
        count = index
        word = ord(word)
        
        while count != 0:
            word += 1
            if word > ord('z'):
                word = word - ord('z') + ord('a') -1
            if word in skip:
                continue
            count -= 1
            
        answer += chr(word)
    return answer