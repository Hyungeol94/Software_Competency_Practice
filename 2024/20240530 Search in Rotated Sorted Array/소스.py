import bisect

class Solution:
    def isSorted(self, left, right, nums):
        if nums[left] < nums[right]:
            return True
        return False

    def findMin(self, left, right, nums):
        mid = (left+right) // 2
        if right-left <= 2:
            valDict = {nums[index]: index for index in [left, mid, right]}
            return sorted(list(valDict.items()), key=lambda a: a[0])[0][1]

        leftSorted = self.isSorted(left, mid, nums)
        rightSorted = self.isSorted(mid, right, nums)

        if leftSorted and rightSorted:
            return left
        
        if not leftSorted and rightSorted:
            return self.findMin(left, mid, nums)

        if leftSorted and not rightSorted:
            return self.findMin(mid, right, nums)

    
    def BinarySearch(self, left, right, target, nums):
        mid = (left+right) // 2
        if right-left <= 2:
            valDict = {nums[index]: index for index in [left, mid, right]}
            return -1 if target not in valDict else valDict[target]

        if nums[mid] == target:
            return mid
        
        elif nums[mid] < target:
            return self.BinarySearch(mid, right, target, nums)
        
        elif nums[mid] > target:
            return self.BinarySearch(left, mid, target, nums)
    

    def search(self, nums: List[int], target: int) -> int:
        minIndex = self.findMin(0, len(nums)-1, nums)
        leftResult = self.BinarySearch(0, minIndex-1, target, nums)
        rightResult =self.BinarySearch(minIndex, len(nums)-1, target, nums)
        return -1 if leftResult == -1 and rightResult == -1 else max(leftResult, rightResult)