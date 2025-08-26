#https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/?envType=daily-question&envId=2025-08-26
#3000. Maximum Area of Longest Diagonal Rectangle

from collections import defaultdict

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        mydict = defaultdict(list)
        for dimension in dimensions:
            l, w = dimension
            mydict[(l**2 + w**2)].append((l, w))
        
        diagonal, rectangles = sorted(mydict.items(), key=lambda a: -a[0])[0]
        maxArea = 0
        for l, w in rectangles:
            maxArea = max(maxArea, l*w)
        return maxArea