#꽉 찬 arr에서 변환하는 함수
def get_index(spell):
    #26진수와 비슷함
    ans = 0
    for i, c in enumerate(spell[::-1]):
        ans += (ord(c) - ord('a') + 1) * (len('abcdefghijklmnopqrstuvwxyz') ** i)
    return ans

def get_string(num):
    #26진수를 구하는 원리와 비슷함
    if num == 0:
        return 'a'
    
    ans = []
    while num:
        num -= 1
        num, remainder = divmod(num, len('abcdefghijklmnopqrstuvwxyz'))
        ans.append(chr(remainder+97))
        
    return ''.join(ans[::-1])


def solution(n, bans):
    arr = sorted([get_index(ban) for ban in bans])
    i = 0
    
    while i != len(arr):
        if arr[i] <= n:
            n += 1
            i += 1
            continue
        else:
            break
    
    return get_string(n)