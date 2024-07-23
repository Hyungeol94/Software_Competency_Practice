from collections import defaultdict

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freqDist = defaultdict(int)
        for num in nums:
            freqDist[num] += 1
        
        answer = []
        for num, freq in sorted(freqDist.items(), key = lambda a: (a[1], -a[0])):
            answer += [num]*freq
        return answer