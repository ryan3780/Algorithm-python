def solution(x, n):
    answer = []
    be = 0
    for i in range(n):
        be += x
        answer.append(be)
    
    return answer