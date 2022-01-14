def solution(n):
    answer = 0
    str_n = str(n)
    str_n_list = [int(i) for i in str_n]
    
    answer = sum(str_n_list)
    
    return answer