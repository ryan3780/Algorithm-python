def solution(n):
    answer = ''
    wm = ''
    
    for i in range(n):
        wm += '수박'
    
    answer = wm[:n]
    
    return answer