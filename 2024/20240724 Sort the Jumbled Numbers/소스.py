#https://leetcode.com/problems/sort-the-jumbled-numbers/?envType=daily-question&envId=2024-07-24

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mydict = dict()
        for i, num in enumerate(mapping):
            mydict[str(i)] = str(num)
        
        arr = []
        for i, num in enumerate(nums):
            convertedNum = ''
            for c in str(num):
                convertedNum += mydict[c]
            arr.append(int(convertedNum))

        arr = {nums[i]: arr[i] for i in range(len(nums))}
        return sorted(nums, key = lambda a: arr[a])