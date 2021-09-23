from sys import stdin

if __name__ == '__main__':
    n, m = map(int, stdin.readline().split())
    strings = {stdin.readline().strip() for _ in range(n)}
    cnt = 0
    
    for _ in range(m):
        pattern = stdin.readline().strip()
        if pattern in strings:
            cnt += 1
    # print(strings)        
    print(cnt)

    