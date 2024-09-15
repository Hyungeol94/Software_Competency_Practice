class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
        i = 0
        n = len(nums)
        
        max_len = 0

        def update():
            nonlocal i, max_len
            count = 0
            while i != len(nums) and nums[i] == max_val:
                count += 1
                max_len = max(max_len, count)
                i += 1
        
        while i < n:
            if nums[i] == max_val:
                update()
            i += 1
        return max_le