#https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/?envType=daily-question&envId=2026-01-15
#2943. Maximize Area of Square Hole in Grid

class Solution:
    def getMaxSequenceLength(self, arr) -> int:
        max_len = 0
        prev = arr[0]
        curr_len = 1
        for num in arr[1:]:
            if prev +1 == num:
                curr_len += 1
            else:
                max_len = max(max_len, curr_len)
                curr_len = 1
            prev = num
        max_len = max(max_len, curr_len)
        return max_len

    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        sorted_h_bars = sorted(hBars)
        sorted_v_bars = sorted(vBars)

        max_h_len = self.getMaxSequenceLength(sorted_h_bars)
        max_v_len = self.getMaxSequenceLength(sorted_v_bars)

        max_len = min(max_h_len, max_v_len)
        return (max_len +1) ** 2