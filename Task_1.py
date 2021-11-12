# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    evens = []
    odds = []
    for num in A:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
            
    ans = 0

    if not evens:
        ans = 0 + max(odds)
    elif not odds:
        ans = 0 + max(evens)
    else:
        ans = max(odds) + max(evens)
        
    return ans
