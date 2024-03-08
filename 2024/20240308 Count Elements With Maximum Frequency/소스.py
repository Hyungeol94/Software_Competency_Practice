#https://leetcode.com/problems/count-elements-with-maximum-frequency/description/

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        num_hash = {}
        for num in nums:
            num_hash[num] = num_hash[num]+1 if num_hash.get(num) else 1
        arr = sorted(list(num_hash.items()), key=lambda a: -a[1])
        freq = 0
        i = 0
        while i < len(arr):
            if arr[i][1] == arr[0][1]:
                freq += arr[0][1]
                i+= 1
            else:
                break
        return freq
            