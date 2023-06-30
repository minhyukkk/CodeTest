def solution(number, limit, power):
    answer = 0
    
    for i in range(1, number+1):
        count = 0
        for j in range(1, int(i**(1/2) +1)):
            if i % j == 0:
                count += 1
                if j**2 != i: #제곱이 되는 약수 중복 방지
                    count+=1
        if count > limit:
            count = power
            answer += count
        else :
            answer += count
    return answer