#https://leetcode.com/problems/trionic-array-ii/?envType=daily-question&envId=2026-02-04
#3640. Trionic Array II
from copy import deepcopy

class Solution: 
    def getMaxSumForThisIndices(self, nums, indices: List[int], prefixSum: List[int]) -> int:
        #햄버거를 구하고, maxSum return하기
        #(udududududud 식으로 인덱스 저장되어 있음) -> index jump를 통해서 햄버거 구하기
        n = len(nums)
        maxSum = -float('inf')

        for i in range(0, len(indices)-2, 2):
            left, mid, right = indices[i], indices[i+1], indices[i+2]
            if not left < mid < right:
                continue    
        
            leftSum = -float('inf')
            for l in range(left, mid):
                leftSum = max(leftSum, prefixSum[mid-1]-prefixSum[l-1] if l > 0 else prefixSum[mid-1 ])
                
            rightSum = -float('inf')
            r = right+1
            prev = nums[right]
            while r < n and prev < nums[r]:
                rightSum = max(rightSum, prefixSum[r]-prefixSum[right-1] if right > 0 else prefixSum[r])
                prev = nums[r]
                r += 1

            middleSum = prefixSum[right-1]-prefixSum[mid-1] if mid > 0 else prefixSum[right]
            maxSum = max(maxSum, leftSum+middleSum+rightSum)

        return maxSum
    


    def maxSumTrionic(self, nums: List[int]) -> int:
        #풀이계획
        #오른쪽으로 이동하면서 trionic array 찾기 (sliding window처럼)
        #upward - downward - upward 반복 => 햄버거 찾기 => maxSum 찾기
        #햄버거 저장 방식
            #시작 인덱스 저장(udududududud 식으로) -> index jump를 통해서 햄버거 구하기
            #중간에 이전 값과 동일한 값 만나면 cleanup

        prev = None
        is_upward = True
        group_indices = []
        curr_indices = [0]

        for i, num in enumerate(nums):
            if prev == num:
                #index 다 지우고, 현재 buffer 넣기
                group_indices.append(deepcopy(curr_indices))
                curr_indices = [i]
                is_upward = True

            if is_upward:
                if prev is not None and prev > num: 
                    is_upward = not is_upward
                    curr_indices.append(i-1)
                prev = num

            else:
                if prev is not None and prev < num:
                    is_upward = not is_upward
                    curr_indices.append(i-1)
                prev = num
        group_indices.append(curr_indices)
        
        #prefixSum 구하기
        acc = 0
        prefixSum = []
        for num in nums:
            acc += num
            prefixSum.append(acc)
    

        #시작 인덱스 구함
        maxSum = -float('inf')

        for indices in group_indices:
            if len(indices) < 3:
                continue

            maxSum = max(maxSum, self.getMaxSumForThisIndices(nums, indices, prefixSum))
        
        return maxSum