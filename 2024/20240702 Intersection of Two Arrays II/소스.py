from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Hash = set(nums1)
        nums2Hash = set(nums2)

        freqDist1 = defaultdict(int)
        freqDist2 = defaultdict(int)

        for num in nums1:
            freqDist1[num] += 1

        for num in nums2:
            freqDist2[num] += 1 
        
        freqDist = defaultdict(int)
        for num in (nums1Hash & nums2Hash):
            freqDist[num] = min(freqDist1[num], freqDist2[num])
        
        answer = []
        for num, freq in freqDist.items():
            for _ in range(freq):
                answer.append(num)
        
        return answer