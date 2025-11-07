#https://leetcode.com/problems/maximize-the-minimum-powered-city/?envType=daily-question&envId=2025-11-07
#2528. Maximize the Minimum Powered City

import copy
import bisect

class Solution:
    def isPossible(self, arr, r, k, target): 
        #greedy approach
        i = 0
        acc = 0
        diffs = copy.copy(arr)
        n = len(diffs)-1
        arr = []
        while i < n:
            acc += diffs[i]
            if acc < target:
                if k < target-acc:
                    return True #정렬을 위해 False일 때 return True
                k -= (target-acc)
                diffs[i] += (target-acc)
                diffs[min(len(diffs)-1, i+2*r+1)] -= (target-acc)
                acc = target 
            arr.append(acc)
            i += 1

        return False


    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)

        diffs = [0]*(n+1)
        for i, station in enumerate(stations):
            left = max(0, i-r)
            right = min(n, i+r+1)
            diffs[left] += station
            diffs[right] -= station
        
        #binary search => range: min~ max power => isPossible로 문제 전환
        acc = 0
        i = 0
        arr = []
        while i < n:
            acc += diffs[i]
            arr.append(acc)
            i += 1 
        
        minVal = min(arr)
        maxVal = sum(stations)+k

        index = bisect.bisect_right(range(minVal, maxVal+1), False, key=lambda a: self.isPossible(diffs, r, k, a))
        return minVal+index-1