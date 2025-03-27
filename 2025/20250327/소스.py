#https://leetcode.com/problems/minimum-index-of-a-valid-split/description/?envType=daily-question&envId=2025-03-27
#2780. Minimum Index of a Valid Split

from collections import defaultdict

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        #valid split을 찾으라
        leftFreqDist = defaultdict(int)
        rightFreqDist = defaultdict(int)

        left_doms = []
        right_doms = []

        dom_key, dom_val = -1, -1
        #왼쪽으로 슬라이딩
        for i, num in enumerate(nums):
            leftFreqDist[num] += 1
            if ((i+1) / 2) < leftFreqDist[num]: #변화된 건 이거밖에 ..
                dom_key = num
                dom_val = leftFreqDist[num]
            
            if not ((i+1) / 2) < dom_val:
                dom_key = -1
                dom_val = -1
            
            left_doms.append(dom_key)
        
        #오른쪽으로 슬라이딩
        dom_key, dom_val = -1, -1
        count = 0
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            rightFreqDist[num] += 1
            count += 1
            if (count / 2) < rightFreqDist[num]: #변화된 건 이거밖에 ..
                dom_key = num
                dom_val = rightFreqDist[num]
            
            if not (count / 2) < dom_val:
                dom_key = -1
                dom_val = -1
            
            right_doms.append(dom_key)

        right_doms = right_doms[::-1]

        #일치하는 값 구하기
        for i in range(len(nums)-1):
            if left_doms[i] == right_doms[i+1]:
                if left_doms[i] != -1:
                    return i
        return -1