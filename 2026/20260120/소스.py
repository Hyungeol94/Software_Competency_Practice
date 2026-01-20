#https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/?envType=daily-question&envId=2026-01-20
#3314. Construct the Minimum Bitwise Array I

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        mymap = {}
        
        for i in range(1, 1001):
            temp = i | (i+1)
            if temp in mymap:
                continue
            mymap[temp] = i

        return list(map(lambda num: mymap[num] if num in mymap else -1, nums))