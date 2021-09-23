import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for i in range(n)]

numbers = sorted(numbers)

print(round(sum(numbers) / n))
print(numbers[n // 2])

_dict = Counter(numbers)
_list = [ k for k, v in _dict.items() if v == max(_dict.values())]
# print('???', _list)
if len(_list) == 1:
    print(_list[0])
else:
    print(_list[1])

print(max(numbers) - min(numbers))