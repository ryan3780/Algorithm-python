# 다른 사람의 풀이
import sys
import re
input = sys.stdin.readline
 
words = input()
ans = ''
tmp = ''
flag = 0

for i in words:
    if i=='<': 
        flag=1 
        ans+=tmp[::-1] 
        tmp='' 
        ans+=i 
    elif i=='>':
        flag=0 
        ans+=i
    elif flag==1:
        ans+=i 
    elif i==' ': 
        ans+=tmp[::-1] 
        ans+=' ' 
        tmp='' 
    elif flag==0: 
        tmp+=i


print(ans)