#https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/editorial/?envType=daily-question&envId=2025-09-03
#3027. Find the Number of Ways to Place People II

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
        
        sorted_key = sorted([key for key, value in mydict.items()])

        num_square = 0
        for point in points:
            x, y = point

            lower_bound = y
            upper_bound = float('inf')
            x_index = sorted_key.index(x)
            i = x_index

            while i >= 0:
                y_array = mydict[sorted_key[i]]
                n = len(y_array)
                y_index = bisect.bisect_left(y_array, lower_bound)
                if i == x_index:
                    if y_index < n-1:    
                        num_square += 1
                        upper_bound = y_array[y_index+1]

                else:
                    if y_index <= n-1:
                        if lower_bound <= y_array[y_index] < upper_bound:
                            upper_bound = y_array[y_index]
                            num_square += 1
                i -= 1
        
        return num_square 