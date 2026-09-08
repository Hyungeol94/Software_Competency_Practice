#https://leetcode.com/problems/construct-uniform-parity-array-ii/?envType=daily-question&envId=2026-09-03
#3876. Construct Uniform Parity Array II

import bisect

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd_prefixes = []
        n = len(nums1)
        if n == 1:
            return True

        arr = sorted(nums1)    
        odd_acc = 0
        for num in arr:         
            if num % 2 == 1:
                odd_acc += 1
            odd_prefixes.append(odd_acc)
        
        #짝수 가능 여부
        is_even_possible = True
        for i, num in enumerate(nums1):
            if num % 2 == 0:
                continue

            index = bisect.bisect_left(arr, num)
            if index == 0:
                is_even_possible = False
                break
            
            else:
                if odd_prefixes[index-1] == 0:
                    is_even_possible = False
                    break

        #홀수 가능 여부
        is_odd_possible = True        
        for i, num in enumerate(nums1):
            if num % 2 == 1:
                continue
            
            index = bisect.bisect_left(arr, num)
            if index == 0:
                is_odd_possible = False
                break
            
            else:
                if odd_prefixes[index-1] == 0:
                    is_odd_possible = False
                    break
        
        return is_even_possible or is_odd_possible