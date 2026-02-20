#https://leetcode.com/problems/special-binary-string/?envType=daily-question&envId=2026-02-20
#761. Special Binary String

class Solution:
    def getSortedMountains(self, s) -> str: #들어오는건 special string => sort
        height = 0
        heights = []

        for i, c in enumerate(s):
            height += (-1 if c is '0' else 1)
            heights.append(height)
        
        heights.pop()
        if len(heights) == 1:
            return "10"

        minVal = min(heights)
        if minVal != 0:
            return s[0] + self.getSortedMountains(s[1:-1]) + s[-1]
        
        heights.append(0)
        heights = list(map(lambda a: str(a), heights))

        prev = 0
        arr = []
        for i, height in enumerate(heights):
            if height == '0':
                arr.append(''.join(s[prev:i+1]))
                prev = i+1
        
        arr = list(map(lambda a: self.getSortedMountains(a), arr))
        arr.sort(reverse=True)
        return ''.join(arr)


    def makeLargestSpecial(self, s: str) -> str:
        #while으로 반복
        #1으로 시작하는, special substring을 구하기 => consecutive? => 교환 가능하다면 바꾸기
        return self.getSortedMountains(s)
