#https://leetcode.com/problems/longest-nice-subarray/?envType=daily-question&envId=2025-03-18
#2401. Longest Nice Subarray

import bisect

class Solution:
    def isNice(self, nums, k): #k length의 Nice한 array가 있는지?
        freqDist = defaultdict(int)
        for i, num in enumerate(nums):
            binary_string = bin(num)[2:]
            binary_string = '0'*(30-len(binary_string)) + binary_string
            for j, c in enumerate(binary_string): #30까지 제한됨
                if c == '1':
                    freqDist[j] += 1

            if i < k:
               continue

            if all(val <= 1 for key, val in freqDist.items()):
                print(k, True)
                return True

            #맨 끝에 있는 것 지우기
            binary_string = bin(nums[i-k])[2:]
            binary_string = '0'*(30-len(binary_string)) + binary_string
            for j, c in enumerate(binary_string): #30까지 제한됨
                if c == '1':
                    freqDist[j] -= 1
            
        return False

    def longestNiceSubarray(self, nums: List[int]) -> int:
        #the length of the longest nice subarray cannot exceed 30.
        # False False True True True True

        idx = bisect.bisect_left(range(min(30, len(nums)), -1, -1), True, key=lambda a: self.isNice(nums,a))
        return min(30, len(nums))-idx+1