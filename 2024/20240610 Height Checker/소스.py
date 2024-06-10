class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights) 
        count = 0 
        for real_height, expected_height in zip(heights, expected):
            if real_height != expected_height:
                count += 1
        return count  