def solution(new_id):
    ans = ''
    new_id = new_id.lower()

    for i in new_id:
        if i.isalpha() or i.isdigit() or i in ['-', '_', '.']:
            ans += i

    while '..' in ans:
        ans = ans.replace('..', '.')

    if len(ans) != 0 and ans[0] == '.':
        ans = ans[1:]
    if len(ans) != 0 and ans[-1] == '.':
        ans = ans[:-1]
    
    if len(ans) == 0:
        ans = 'a'
    if len(ans) > 15:
        ans = ans[:15]
        if ans[-1] == '.':
            ans = ans[:-1]
            
    if len(ans) <= 2:
        while len(ans) <= 2:
            ans += ans[-1]
    
    return ans