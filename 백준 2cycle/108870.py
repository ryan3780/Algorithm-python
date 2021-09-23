import sys
from collections import Counter

input = sys.stdin.readline

n = int(input().rstrip())

_list = list(map(int, input().split()))

p_list = sorted(set(_list))

p_dict = {val : idx for idx, val in enumerate(p_list)}


for i in _list:
    print(p_dict[i], end= ' ')
