import sys

input = sys.stdin.readline

nums = input().rstrip()

dials = {2 : 'abc', 3 : 'def', 4 : 'ghi' , 5: 'jkl' ,6 :'mno' , 7 : 'pqrs', 8 : 'tuv' , 9: 'wxyz'}

ans = 0
for i in nums.lower():
    for k, v in dials.items():
        if i in v:
            ans += k

print(ans + len(nums))