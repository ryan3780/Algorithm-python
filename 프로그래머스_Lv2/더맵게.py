from collections import deque

def solution(scoville, K):
    answer = 0
    k = K
    scv = deque(sorted(scoville))
    cnt = 0
    
    while scv[0] < k:
        
        mix = scv.popleft() + (scv.popleft() * 2)
        scv.appendleft(mix)
        sorted(scv)
        print(scv)
        cnt += 1
                
    return answer