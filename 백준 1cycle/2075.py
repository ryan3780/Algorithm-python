import sys
import heapq

input = sys.stdin.readline

N = int(input().strip())

nxn = []

for i in range(N):                              # N
    numbers = list(map(int,input().split()))
    for j in range(N):                          # N
        if len(nxn) == N:
            min_num = heapq.heappop(nxn)
            if min_num < numbers[j]:
                # print(min_num, numbers[j])
                heapq.heappush(nxn, numbers[j])
            else:
                heapq.heappush(nxn, min_num)
        else:
            heapq.heappush(nxn, numbers[j])
               
print(heapq.heappop(nxn))               # O(N^2)