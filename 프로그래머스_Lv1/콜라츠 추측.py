cnt = 0 
answer = 0

def solution(num):
    
    global cnt, answer
    
    if num == 1:
        return cnt
    
    if num % 2 == 0:
        answer = num // 2
    if num % 2 == 1:
        answer = num * 3 + 1
    
    cnt += 1
    if cnt == 500:
        return -1
    
    return solution(answer)