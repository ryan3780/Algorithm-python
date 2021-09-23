import sys
from itertools import product

input = sys.stdin.readline

N, M = map(int,input().rstrip().split())

happy = []


for i in range(N):
    K = list(map(int, input().rstrip().split()))
    happy.append(K)

print(happy)