import sys
from collections import deque

input = sys.stdin.readline

total_test = int(input())

for i in range(total_test):
    n, m = map(int, input().split())
    doc = deque(map(int, input().split()))

    cnt = 0

    while doc:
        first = max(doc)
        m -= 1
        last = doc.popleft()
        
        if first != last:
            doc.append(last)
            if m < 0:
                m = len(doc) - 1
        
        else:
            cnt += 1
            if m == -1:
                print(cnt)
                break




        
