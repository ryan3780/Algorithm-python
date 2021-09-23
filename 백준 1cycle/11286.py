import sys
import heapq

input = sys.stdin.readline

N = int(input().strip())
heap = []

for i in range(N):
    num = int(input().strip())
    print(heap)
    if num == 0:
        if heap:
            print('ans',heapq.heappop(heap)[1])
        else:
            print('ans',0)
    else:
        heapq.heappush(heap, (abs(num),num))
