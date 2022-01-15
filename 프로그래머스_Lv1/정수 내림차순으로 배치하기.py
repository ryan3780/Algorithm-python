def solution(n):
    answer = 0
    str_n = sorted(str(n), reverse=True)
    answer = int(''.join(str_n))
    return answer