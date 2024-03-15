#https://leetcode.com/problems/product-of-array-except-self/description/?envType=daily-question&envId=2024-03-15

from collections import deque
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i]*prefix[i-1])
        suffix = deque([nums[-1]])
        for i in range(len(nums)-2, -1, -1):
            suffix.appendleft(nums[i]*suffix[0])
        n = len(nums)
        answer = [suffix[1]]
        for i in range(1, n-1):
            answer.append(prefix[i-1] * suffix[i+1])
        answer.append(prefix[n-2])
        return answer


        