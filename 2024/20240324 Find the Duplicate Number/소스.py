class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        check = 0
        for num in nums:
            if check & (1 << num):
                return num
            else:
                check = check | (1 << num)
          