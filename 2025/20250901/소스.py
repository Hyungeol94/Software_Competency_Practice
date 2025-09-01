#https://leetcode.com/problems/maximum-average-pass-ratio/description/?envType=daily-question&envId=2025-09-01
#1792. Maximum Average Pass Ratio

import heapq

class Solution:
    def getGap(self, numerator, denominator):
        return ((numerator+1) / (denominator+1)) - (numerator / denominator)

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        heapq.heapify(heap)
        for i, (num_pass, total) in enumerate(classes):
            heapq.heappush(heap, (-self.getGap(num_pass, total), num_pass, total))
        
        i = extraStudents
        while i > 0:
            _, num_pass, total = heapq.heappop(heap)
            heapq.heappush(heap, (-self.getGap(num_pass+1, total+1), num_pass+1, total+1))
            i-= 1
        
        sum_ratio = 0
        while heap:
            _, num_pass, total = heapq.heappop(heap)
            sum_ratio += (num_pass / total)
        
        return sum_ratio / len(classes)