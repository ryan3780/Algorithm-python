def solution(s):
    answer = ''
    words = s.split(' ')
    for i in words:
        answer += ' '
        for j in range(len(i)):
            if j % 2 == 1:
                answer += i[j].lower()
            else:
                answer += i[j].upper()
    
    return answer[1:]