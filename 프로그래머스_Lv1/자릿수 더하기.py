def solution(n):
    answer = 0
    str_n = str(n)
    str_n_list = []
    
    for i in str_n:
        str_n_list.append(int(i))
    
    answer = sum(str_n_list)
    
    return answer