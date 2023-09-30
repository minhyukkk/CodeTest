def solution(picks, minerals):
    answer = 0
    
    sum =0
    # 곡괭이의 수를 구한다.
    for i in picks:
        sum += i
    
    #곡괭이로 캘 수 있는 광물만큼 자른다.
    num = sum * 5
    if len(minerals)>sum:
        minerals = minerals[:num]
        
    array = [[0,0,0] for _ in range(len(minerals) // 5 +1)]
    
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            array[i//5][0] += 1
        if minerals[i] == 'iron':
            array[i//5][1] += 1
        if minerals[i] == 'stone':
            array[i//5][2] += 1
    
    array.sort(key = lambda x : (-x[0], -x[1], -x[2]))
    
    for i in array:
        dia, iron, stone = i
        
        for j in range(len(picks)):
            if picks[j] > 0 and j == 0:
                picks[j] -= 1
                answer += dia + iron + stone
                break
                
            elif picks[j] > 0 and j == 1:
                picks[j] -= 1
                answer += (dia * 5) + iron + stone
                break
                
            elif picks[j] > 0 and j == 2:
                picks[j] -= 1
                answer += (dia *25) + (iron *5) + stone
                break
    
    return answer