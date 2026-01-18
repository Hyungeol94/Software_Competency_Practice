#https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/?envType=daily-question&envId=2026-01-17
#3047. Find the Largest Area of Square Inside Two Rectangles

class Solution:
    def getIntersectSize(self, bottomLeft, topRight, i, j) -> int: 
        rect1_x_range = [bottomLeft[i][0], topRight[i][0]]
        rect1_y_range = [bottomLeft[i][1], topRight[i][1]]

        rect2_x_range = [bottomLeft[j][0], topRight[j][0]]
        rect2_y_range = [bottomLeft[j][1], topRight[j][1]]

        #rect1이 x기준 더 빠른 시작하도록 설정
        if rect1_x_range[0] > rect2_x_range[0]:
            rect1_x_range, rect2_x_range = rect2_x_range, rect1_x_range 
        
        if rect1_x_range[1] <= rect2_x_range[0]:
            return 0

        x_overlap_start = max(rect1_x_range[0], rect2_x_range[0])
        x_overlap_end = min(rect1_x_range[1], rect2_x_range[1])
        x_overlap_length = x_overlap_end-x_overlap_start
    
        if rect1_y_range[0] > rect2_y_range[0]:
            rect1_y_range, rect2_y_range = rect2_y_range, rect1_y_range
        
        if rect1_y_range[1] <= rect2_y_range[0]:
            return 0
        
        y_overlap_start = max(rect1_y_range[0], rect2_y_range[0])
        y_overlap_end = min(rect1_y_range[1], rect2_y_range[1])
        y_overlap_length = y_overlap_end-y_overlap_start
        
        return min(x_overlap_length, y_overlap_length) ** 2

    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        #10^3 => 1000000 => 100만
        #O(n^2)로 풀이 가능
        maxVal = -float('inf')
        n = len(bottomLeft)
        for i in range(n-1):
            for j in range(i+1, n):
                maxVal = max(maxVal, self.getIntersectSize(bottomLeft, topRight, i, j))

        return maxVal