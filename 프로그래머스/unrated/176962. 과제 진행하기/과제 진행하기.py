def solution(plans):
    answer = []
    
    for i in range(len(plans)):
        h,m = map(int, plans[i][1].split(':'))
        st = h*60+m
        plans[i][1] = st
        plans[i][2] = int(plans[i][2])
        
    stack = []
    plans.sort(key = lambda x: x[1])
    
    for i in range(len(plans)):
        if i == len(plans) -1:
            stack.append(plans[i])
            break
            
        sub, st, t = plans[i]
        nsub, nst, nt = plans[i+1]
        
        if st + t <= nst:
            temp_time = nst - (st + t)
            answer.append(sub)
            
            while temp_time !=0 and stack:
                tsub, tst, tt = stack.pop()
                if temp_time >= tt:
                    temp_time -= tt
                    answer.append(tsub)
                else:
                    stack.append([tsub, tst, tt - temp_time])
                    temp_time = 0

        else:
            plans[i][2] = t - (nst-st)
            stack.append(plans[i])
        
    while stack:
        sub, st, t = stack.pop()
        answer.append(sub)
    
    return answer