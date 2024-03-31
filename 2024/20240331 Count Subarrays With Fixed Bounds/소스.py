from copy import deepcopy
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        freqDist = {}
        left = 0
        right = 0
       
        count = 0
        while right<len(nums):
            freqDist[nums[right]] = 1 if nums[right] not in freqDist else freqDist[nums[right]]+1
            if minK not in freqDist or maxK not in freqDist:
                if minK <= min(freqDist) and max(freqDist) <= maxK:
                    right += 1
                    continue

            if min(freqDist) == minK and max(freqDist) == maxK:
                minKcount = freqDist[minK]
                maxKcount = freqDist[maxK]
                temp = left
                while minKcount != 0 and maxKcount != 0 and temp <= right:
                    count += 1
                    if nums[temp] == minK:
                        minKcount -= 1
                    if nums[temp] == maxK:
                        maxKcount -= 1
                    temp += 1
                right += 1
                continue

            else:
                left = right+1
                right = left
                freqDist = {}
        
        return count
