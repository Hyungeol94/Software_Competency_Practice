#https://leetcode.com/problems/zero-array-transformation-ii/?envType=daily-question&envId=2025-03-13
#3356. Zero Array Transformation II

from copy import copy

class Solution:
    def isZero(self, i):
        acc = 0

        diffs = [0]*(len(self.nums)+1)
        prefix = 0
        prefixes = []
        for query in self.queries[:i+1]: #O(n)
            left, right, val = query
            diffs[left] -= val
            diffs[right+1] += val

        offsets = []
        for diff in diffs:
            acc += diff
            offsets.append(acc)
        
        for num, offset in zip(self.nums, offsets):
            if max(0, num+offset) != 0:
                return False
        return True

    def binarySearch(self, left, right):
        if left >= right:  # Base case to stop recursion
            return left if self.isZero(left) else -1

        mid = (left + right) // 2 
        
        if self.isZero(mid):
            return self.binarySearch(left, mid)
        
        else:
            return self.binarySearch(mid+1, right)


    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        self.nums = nums
        self.queries = queries

        if all([num == 0 for num in nums]):
            return 0

        #O(nlogn)
        res = self.binarySearch(0, len(queries)-1) 
        return res+1 if res != -1 else -1
    
    def minZeroArray2(self, nums: List[int], queries: List[List[int]]) -> int:
        self.nums = nums
        self.queries = queries

        if all(num == 0 for num in nums):
            return 0

        # bisect 함수 사용 가능
        # lambda a: self.isZero(a)를 적용해 map했을 때 [False, False, ... True, True] 식으로 정렬될 것이기 때문임
        idx = bisect_left(range(len(queries)), True, key=self.isZero)
        return idx + 1 if idx < len(queries) else -1

