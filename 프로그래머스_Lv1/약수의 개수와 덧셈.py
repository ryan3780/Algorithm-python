def solution(left, right):
    answer = []
    div= {}

    for i in range(left, right+1):
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
                div[i] = cnt
    for k, v in div.items():
        if v % 2 != 0:
            k = -k

        answer.append(k)

    answer = sum(answer)

    return answer