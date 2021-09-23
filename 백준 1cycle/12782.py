import sys

input = sys.stdin.readline

N = int(input())

for i in range(N):
    a, b = input().rstrip().split()
    one, zero = 0, 0 

    for idx, num in enumerate(a):
        if num != b[idx]:
            if num == '1':
                one += 1
            else:
                zero += 1

    print(max(one, zero))