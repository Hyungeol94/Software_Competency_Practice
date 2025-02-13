#https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/description/
#3066. Minimum Operations to Exceed Threshold Value II

import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        for num in nums:
            heapq.heappush(heap, num)
        
        count = 0
        while heap:
            val1 = heapq.heappop(heap)
            if k <= val1:
                return count
            val2 = heapq.heappop(heap)
            count += 1
            heapq.heappush(heap, val1*2 + val2)

        return count