def solution(answers):
    answer = [0,0,0]
    ans = []
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5,]
    
    for i in range(len(answers)):
        if answers[i] == s1[(i% len(s1))]:
            answer[0] += 1
        if answers[i] == s2[(i% len(s2))]:
            answer[1] += 1
        if answers[i] == s3[(i% len(s3))]:
            answer[2] += 1
            
    for i in range(3):
        if answer[i] == max(answer):
            ans.append(i+1)

    return ans