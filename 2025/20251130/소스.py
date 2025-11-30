#https://leetcode.com/problems/make-sum-divisible-by-p/?envType=daily-question&envId=Invalid%20Date
#1590. Make Sum Divisible by P

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        remainder = sum(nums) % p
        if remainder == 0:
            return 0
        
        acc = 0
        prefixSums = []
        for num in nums:
            acc += num
            prefixSums.append(acc)
        
        prevs = {}
        minLen = float('inf')
        sumNums = sum(nums)
        for i, prefixSum in enumerate(prefixSums):
            #remainder + p*n 만큼 덜어내야 함
            #뒤에 있는 것을 뺐을 때, remainder + p*n이 남을 수 있어야 함
            #뒤에 있는 것을 뺀 것에 %p를 했을 때 remainder가 남아야 함
            #(prefixSum-x) % p = remainder
            #단번에 키값으로 찾는 방법 ?
            #키값 => rem 
            #((p*n + rem1) - (q*n + rem2)) % p = remainder
            #(rem1 - rem2) % p = remainder
            #현재 rem을 기준으로 rem2를 찾는 방법 ?
            #rem2 = (rem1 - remainder + p) % p
            if i!= len(nums)-1 and (sumNums - prefixSum) % p == 0:
                minLen = min(minLen, i+1)
            rem1 = prefixSum % p
            prevs[rem1] = i
            rem2 = (rem1 - remainder + p) % p
            if rem2 not in prevs:
                continue
            minLen = min(minLen, i-prevs[rem2])

        return minLen if minLen != float('inf') else -1