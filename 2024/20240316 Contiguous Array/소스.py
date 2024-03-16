#https://leetcode.com/problems/contiguous-array/description/?envType=daily-question&envId=2024-03-16
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        zero_acc, one_acc = [0]*n, [0]*n
        zero_acc[0] = 1 if nums[0] == 0 else 0
        one_acc[0] = 1 if nums[0] == 1 else 0

        for i in range(1, n):
            zero_acc[i] = zero_acc[i-1]+1 if nums[i] == 0 else zero_acc[i-1]
            one_acc[i] = one_acc[i-1]+1 if nums[i] == 1 else one_acc[i-1]
        
        for i in reversed(range(n)):
            if zero_acc[i] == one_acc[i]:
                return i+1

        maxLen = 0
        for i in range(1, n-1):
            for j in range(i+1, n):
                #i에서 j까지
                if zero_acc[j]-zero_acc[i-1] == one_acc[j]-one_acc[i-1]:
                    maxLen = max(maxLen,j-i+1)
        return maxLen

                    

        
       

        