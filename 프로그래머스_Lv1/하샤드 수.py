def solution(x):
    answer = True
    
    str_x = str(x)
    total = sum([int(x) for x in str_x])
    
    if x % total != 0:
        return False
    
    return answer