def solution(n):
    answer = []
    str_n = str(n) 
    answer = [int(i) for i in str_n[::-1]]
    
    return answer