from copy import deepcopy
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:

        # freqDist = {}
        numSet = set()
        left = 0
        right = 0       
        count = 0
      
        sliding_start = 0
        minIndex = -1
        maxIndex = -1

        while right<len(nums):
            numSet.add(nums[right])
            if nums[right] < minK or maxK < nums[right]:
                left = right+1
                right = left
                # minIndex = -1
                # maxIndex = -1
                sliding_start = left
                numSet = set()
                continue

            if nums[right] == minK:
                minIndex = right
                #여기에서 window_start를 업데이트!
                #sliding_start와 right 사이에 있는 minK와 maxK의 인덱스 중 더 작은 곳의 위치로 업데이트
                sliding_start = min(minIndex, maxIndex)
            if nums[right] == maxK:
                maxIndex = right
                sliding_start = min(minIndex, maxIndex)
            
            if minK not in numSet or maxK not in numSet:
                sliding_start += 1
                if minIndex < left or maxIndex < left:
                    right += 1                    
                    continue


            if min(numSet) == minK and max(numSet) == maxK:
                count += sliding_start-left+1
                right += 1
                continue

            else:
                left = right+1
                right = left
                sliding_start = left
                numSet = set()
        
        return count
