#https://leetcode.com/problems/count-subarrays-with-score-less-than-k/description/?envType=daily-question&envId=2025-04-28
#2302. Count Subarrays With Score Less Than K

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        #sliding window
        #contiguous해야 함
        #nums[0]을 반드시 포함
        #nums[1]을 반드시 포함
        #nums[2]를 반드시 포함.. 
        #길이가 나오면 그 이하 subarray를 모두 구하면 됨
        i = 0
        j = 0
        product = 1
        arrlen = 0
        count = 0
        n = len(nums)
        while i < n: 
            product = ((product / arrlen) + nums[i]) * (arrlen + 1) if i != 0 else nums[0]
            arrlen += 1
            while j < i and k <= product:
                product = ((product / arrlen) - nums[j]) * (arrlen - 1)
                arrlen -= 1
                j += 1
            offset = arrlen if product < k else 0
            count += offset
            i += 1
        return count