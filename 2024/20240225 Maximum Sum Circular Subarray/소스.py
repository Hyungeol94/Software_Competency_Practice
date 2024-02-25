#Maximum Sum Circular Subarray

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        left = 0
        right = 0
        currentSum = 0
        maxSum = -float('inf')
        n = len(nums)
        limit = 2*n
        if n == 1:
            return nums[0]

        while True:
            if currentSum < 0:
                left = right % n 
                currentSum = nums[left]
                maxSum = max(maxSum, currentSum)
                right += 1
                if right == limit:
                    return maxSum
                continue
            
             #인덱스가 겹치는지 확인
            if n <= right and left == right % n:
                currentSum -= nums[left]
                maxSum = max(currentSum, maxSum)        
                left += 1
                if left < n:
                    continue
                return maxSum

            else:
                #겹치지 않을 때 
                currentSum += nums[right % n]
                maxSum = max(currentSum, maxSum)        
                right += 1
                if right == limit:
                    return maxSum

            
                    

    

                
                
        



        

