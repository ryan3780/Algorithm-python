import sys
from itertools import product

input = sys.stdin.readline

N, M = map(int,input().rstrip().split())

K = list(map(str, input().rstrip().split()))

# 값을 깍으려면 input의 숫자를 그대로 대입하면 안된다.
_len = len(str(N))

while True:
    products = list(product(K, repeat=_len))
    result = []
    for i in products:
        comp = int("".join(i))
        if comp <= N:
            result.append(comp)
            
    if len(result) >= 1:
        print(max(result))
        break
    else:
        _len -= 1  


