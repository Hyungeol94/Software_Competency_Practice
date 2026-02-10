#https://leetcode.com/problems/longest-balanced-subarray-i/?envType=daily-question&envId=2026-02-10
#3719. Longest Balanced Subarray I

from collections import defaultdict
from copy import deepcopy

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        dict_nums = defaultdict(int)
        prefix_dict = []
        for num in nums:
            dict_nums[num] += 1
            prefix_dict.append(deepcopy(dict_nums))
        
        for k in range(n-1, 0, -1):
            i = 0
            curr_dict = prefix_dict[i+k]
            num_odd = 0
            num_even = 0
            for num, count in curr_dict.items():
                if num % 2 == 0:
                    num_even += 1
                else:
                    num_odd += 1
            
            if num_even == num_odd:
                return k+1

            while i+k < n:
                left_num = nums[i]
                curr_dict[left_num] -= 1
                if curr_dict[left_num] == 0:
                    if left_num % 2 == 0:
                        num_even -= 1
                    else:
                        num_odd -= 1
                    
                i+= 1
                if i+k >= n:
                    break
                right_num = nums[i+k]
                curr_dict[right_num] += 1
                if curr_dict[right_num] == 1: #추가했는데 1이 된다면 늘어난 것
                    if right_num % 2 == 0:
                        num_even += 1
                    else:
                        num_odd += 1
                
                if num_even == num_odd:
                    return k+1

        return 0