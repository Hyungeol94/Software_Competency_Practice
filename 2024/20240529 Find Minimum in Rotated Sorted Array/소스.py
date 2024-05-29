class Solution:
    def findMin(self, nums: List[int]) -> int:
        def isSorted(left, right, nums):
            if nums[left] < nums[right]:
                return True
            return False
        
        def binarySearch(left, right, nums):
            mid = (left+right) // 2
            leftSorted = isSorted(left, mid, nums)
            rightSorted = isSorted(mid, right, nums)
            if right-left <= 2:
                return min(nums[left], nums[mid], nums[right])
                
            if leftSorted and rightSorted:
                return nums[left]
            
            if leftSorted and not rightSorted:
                return binarySearch(mid, right, nums)
            
            if not leftSorted and rightSorted:
                return binarySearch(left, mid, nums)

        return binarySearch(0, len(nums)-1, nums)