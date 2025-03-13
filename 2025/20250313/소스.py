#3355. Zero Array Transformation I

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        #쿼리 하나에 O(1)으로 할 수 있는 방법? ➡️ difference array 사용
        diffs = [0]*(len(nums)+1)

        for query in queries:
            left, right = query
            diffs[left] -= 1
            diffs[right+1] += 1

        offsets = []
        offset = 0
        for diff in diffs:
            offset += diff
            offsets.append(offset)
        
        for num, offset in zip(nums, offsets):
            if max(num+offset, 0) != 0:
                return False
        return True
