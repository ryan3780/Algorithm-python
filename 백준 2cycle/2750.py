import sys

input = sys.stdin.readline

n = int(input())

numbers = [0] * 10001

for i in range(n):
    num = int(input())
    numbers[num] = numbers[num] + 1

for i in range(10001):
    if numbers[i] != 0 :
        for j in range(numbers[i]):
            print(i)
