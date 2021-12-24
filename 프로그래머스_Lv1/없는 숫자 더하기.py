def solution(numbers):
    answer = -1
    for i in range(10):
        if i not in numbers:
            answer += i

    return answer

# 눈이 뜨인 해답

def solution(numbers):
    return 45 - sum(numbers)