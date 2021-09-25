import sys

# 입력부
n = sys.stdin.readline().rstrip()
b = int(sys.stdin.readline())

# l_stack : 왼쪽 스택(문자열로 초기화)
# r_stack : 오른쪽 스택
l_stack = list(n)
r_stack = []

for s in range(b):
    # x : 쿼리
    x = sys.stdin.readline().rstrip()
    # 만일 왼쪽으로 이동 시 왼쪽에서 오른쪽으로 옮김
    if x == "L" and l_stack:
        r_stack.append(l_stack.pop())
    # 만일 오른쪽으로 이동 시 오른쪽에서 왼쪽으로 옮김
    elif x == "D" and r_stack:
        l_stack.append(r_stack.pop())
    # 만일 삭제 시 왼쪽에서 하나 삭제
    elif x == "B" and l_stack:
        l_stack.pop()
    # 만일 삽입 시 왼쪽에 문자 삽입
    else:
        if x[0] == "P":
            l_stack.append(x[2])

# 오른쪽 스택을 뒤집어서 왼쪽 스택과 합친 후 출력
print(''.join(l_stack + r_stack[::-1]))