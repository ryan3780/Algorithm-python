import itertools

def solution(nums):
    answer = 0
    
    cnt = list(itertools.combinations(nums,3))
    
    for i in cnt:
        sum_num = sum(i)

        for j in range(2, sum_num):
            if sum_num % j == 0:
                break
                
        else:
            answer += 1
 
    return answer
