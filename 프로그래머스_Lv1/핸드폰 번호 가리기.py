def solution(phone_number):
    
    answer = ''
    len_number = len(phone_number) - 4
    answer = phone_number[-4:]
    ans = ['*' for i in range(len_number)]
    answer = ''.join(ans) + answer
    
    return answer