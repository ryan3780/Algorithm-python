import sys
import math
from itertools import combinations

input = sys.stdin.readline

words = input().rstrip()
items = []
for i in words:
    items.append(i)

combi = []
for i in range(1, len(items)):
    combi= list(map(''.join, combinations(items, i)))


print(combi)

# num = int(input().rstrip())
# books = []



# for i in range(num):
#     price, title = map(str, input().rstrip().split())
#     books.append([price, title])

# result = []
# min_price = math.inf



# print(result)