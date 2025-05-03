#https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/?envType=daily-question&envId=2025-05-03
#1007. Minimum Domino Rotations For Equal Row

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
    #처음 나오는 것 둘 중 하나는 반드시 반복해서 나와야 함
    #그게 무엇인지를 찾기
    #그것의 count를 각각 찾기

        count_a = 0
        count_b = 0
        for top, bottom in zip(tops, bottoms):
            if tops[0] in set([top, bottom]):
                count_a += 1
            if bottoms[0] in set([top, bottom]):
                count_b += 1
        
        n = len(tops)
        if count_a != n and count_b != n:
            return -1
        
        criteria = tops[0] if count_a == n else bottoms[0]
        top_count = 0
        bottom_count = 0
        for top, bottom in zip(tops, bottoms):
            if top == criteria:
                top_count += 1
            if bottom == criteria:
                bottom_count += 1

        return min(top_count, n-top_count, bottom_count, n-bottom_count)