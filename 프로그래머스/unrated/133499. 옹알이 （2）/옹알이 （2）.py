def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    repeats = ["ayaaya", "yeye", "woowoo", "mama"]
    answer = 0
    
    #babbling의 단어를 하나씩 뺴서 repeats와 words의 단어들과 비교
    #예) ayaye = Oye -> OO -> answer +=1
    #예) ayaayaa = Xa
    for x in babbling:
        for word in repeats:
            # replace(변경하고 싶은문자, 변경후 문자)
            # 여기서는 babbling에서 뺀 단어들을 반복되어 있는 문자열과 하나씩 비교에서 있다면 X로 바꾸어줌
            x = x.replace(word, "X")
        for word in words:
            x = x.replace(word, "O")
        
        isValid = True
        for char in x:
            if char != "O":
                isValid = False
                break
                
        if isValid == True:
            answer += 1
    return answer