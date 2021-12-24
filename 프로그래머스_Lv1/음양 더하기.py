def solution(absolutes, signs):
    answer = 0
    
    for i in range(len(absolutes)):
        if signs[i] is False:
            absolutes[i] = '-' + str(absolutes[i])

    ans =  list(map(int, absolutes))
    answer = sum(ans)
    
    return answer