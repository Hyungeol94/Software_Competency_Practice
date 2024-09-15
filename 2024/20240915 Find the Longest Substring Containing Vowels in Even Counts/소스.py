from collections import defaultdict
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        #마스크 만들기
        masks =[]
        mask = 0
        for c in s:
            if c not in ['a', 'e', 'i', 'o', 'u']:
                masks.append(mask)
                continue
            
            index = ['a', 'e', 'i', 'o', 'u'].index(c)
            mask = mask ^ (1 << index)
            masks.append(mask)
        
        print(masks)
        #XOR 연산자로 비트마스킹해서 제일 긴 것 구해보기
        answer = 0
        my_dict = defaultdict(int)
        for i, mask in enumerate(masks):
            if mask not in my_dict:
                my_dict[mask] = i
                continue
            if s[my_dict[mask]] in ['a', 'e', 'i', 'o', 'u']:
                answer = max(answer, i-my_dict[mask])
            else: 
                answer = max(answer, i-my_dict[mask]+1)
            if mask == 0:
                answer = max(answer, i+1)
        return answer
