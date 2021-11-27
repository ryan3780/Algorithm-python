digits = {'ab' : 1, 'cde' : 2, 'fgh' : 3}

arr = [['a','s'], ['s','d'], ['d','f'], ['a','s','d','f']]
ans = [0,0,0,0,0,0,0]
for i in range(len(arr)):
    cnt = 0
    for j in range(len(arr)):
        try:
            # print(arr[i][j])
            for key, val in digits.items():
                if arr[i][j] in key:
                    cnt += val
                    ans[i] = (len(arr[i]), cnt)
                    print(cnt)
        except:
            continue
      
print(ans)