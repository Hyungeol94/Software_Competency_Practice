#https://leetcode.com/problems/find-unique-binary-string/?envType=daily-question&envId=2026-03-08
#1980. Find Unique Binary String

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        max_val = int('0b'+'1'*n, 2)
        nums_set = list(map(lambda a: 
            int('0b' + a, 2), 
            nums))

        for i in range(max_val+1):
            if i not in nums_set:
                return bin(i)[2:].zfill(n)