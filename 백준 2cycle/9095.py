import sys
input = sys.stdin.readline

# DP는 점화식을 구해야 하는건가?

T = int(input()) 
l = [0, 1, 2, 4, 0, 0, 0, 0, 0, 0, 0] 
for _ in range(T):
     n = int(input()) 
     for i in range(4, n+1): 
         l[i] = l[i-1] + l[i-2] + l[i-3] 
         
     print(l[n])

# https://deepwelloper.tistory.com/entry/BOJ-9095-1-2-3-%EB%8D%94%ED%95%98%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%ED%92%80%EC%9D%B4