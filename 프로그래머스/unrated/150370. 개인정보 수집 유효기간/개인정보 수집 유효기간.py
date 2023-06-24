def dateToDay(date):
    year, month, day = map(int, date.split("."))
    return (year * 12 * 28) + (month * 28) + day

def solution(today, terms, privacies):
    answer = []
    
    # today
    today = dateToDay(today)
    
    # terms terms를 딕셔너리로 만들어서 키 값과 밸류값으로 하나씩 분류
    termsInfo = dict()
    for term in terms:
        term = term.split()
        termsInfo[term[0]] = int(term[1]) * 28
        
    # privacies for문을 통해 하나씩 접근하고 위에서 만든 terms를 통해 그 값을 바로 더할 수 있게 함
    for i in range(len(privacies)):
        date, term = privacies[i].split()
        if dateToDay(date) + termsInfo[term] <= today:
            answer.append(i+1)
    return answer