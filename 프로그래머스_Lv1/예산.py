def solution(d, budget):
    answer = 0
    d_sort = sorted(d)
    
    if sum(d) == budget:
        answer = len(d)
        return answer
    
    money = budget
    cnt = 0
    
    for i in d_sort:
        if (money - i) >= 0:
            money -= i
            cnt += 1
    
    answer = cnt
    
    return answer