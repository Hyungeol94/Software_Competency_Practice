#https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/?envType=daily-question&envId=2025-09-02
#3025. Find the Number of Ways to Place People I

from collections import defaultdict
import bisect

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        mydict = defaultdict(list)
        for point in points:
            x, y = point
            mydict[x].append(y)

        for key, value in mydict.items():
            mydict[key] = sorted(value)
        
        num_square = 0
        for point in points:
            x, y = point
            y_array = mydict[x]
            n = len(y_array)
            index = bisect.bisect_left(y_array, y)
            lower_bound = y
            upper_bound = float('inf')

            if index != n-1:
                num_square += 1
                upper_bound = y_array[index+1]

            i = x-1
            while i >= 0:
                y_array = mydict[i]
                index = bisect.bisect_left(y_array, lower_bound)
                if index > len(y_array)-1:
                    i -= 1
                    continue
                
                if lower_bound <= y_array[index] < upper_bound:
                    upper_bound = y_array[index]
                    num_square += 1
                i -= 1
        
        return num_square 