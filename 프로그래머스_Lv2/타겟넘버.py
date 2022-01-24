from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque()
    n = len(numbers)
    q.append([numbers[0], 0])
    