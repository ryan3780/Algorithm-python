import sys
input = sys.stdin.readline

# 이런 식으로도 가능하다 // 다른 사람 코드
a = int(input())
count = 0
minimum=[a]
def cal(a):
    list = []
    for i in a:
        list.append(i-1)
        if i%3 == 0:
            list.append(i/3)
        if i%2 == 0:
            list.append(i/2)
    return list
 
while True:
    if a == 1:
        print(count)
        break
    temp = minimum[:]
    minimum = []
    minimum = cal(temp)
    count +=1
    if min(minimum) == 1:
        print(count)
        break
        
#https://doorbw.tistory.com/57
