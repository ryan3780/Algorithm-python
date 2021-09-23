import sys

input = sys.stdin.readline

n = input().rstrip()

numbers = map(int, list(input().rstrip()))

print(list(numbers))