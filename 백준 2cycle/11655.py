import sys
input = sys.stdin.readline
 
sentence = input().rstrip()
ans = ''
for i in sentence:
    if i.isupper():
        if ord(i) + 13 > 90:
            ans += (chr(ord(i) + 13 - 90 + 64))
        else:
            ans +=(chr(ord(i) + 13))
    elif i.islower():
        if ord(i) + 13 > 122:
            ans += (chr(ord(i) + 13 - 122 + 96))
        else:
            ans += (chr(ord(i) + 13))
    elif i.isspace():
        ans += (' ')
    elif i.isdigit():
        ans += i

print(ans)