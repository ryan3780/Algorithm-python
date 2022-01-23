import heapq

def solution(scoville, K):
    answer = 0
    k = K
    heapq.heapify(scoville)
    
    while scoville[0] < k:
        
        mix = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, mix)
        answer += 1
        
        if len(scoville) == 1 and scoville[0] < k :
            return -1 
                
    return answer