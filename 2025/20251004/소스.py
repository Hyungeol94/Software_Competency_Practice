#https://leetcode.com/problems/container-with-most-water/description/?envType=daily-question&envId=2025-10-04
#11. Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1

        maxArea = 0
        while left < right:
            width = right - left
            maxArea = max(maxArea, width * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea