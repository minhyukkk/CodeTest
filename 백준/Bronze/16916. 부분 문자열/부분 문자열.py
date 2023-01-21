s, p = [input() for _ in range(2)] # range(2)쓰지 않으면 에러

print([0,1][s.__contains__(p)]) # s 문자열에 p라는 문자열이 존재하는지 확인 = contains로
# 존재x -> 0 존재o -> 1