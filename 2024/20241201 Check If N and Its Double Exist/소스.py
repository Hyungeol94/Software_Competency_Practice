#https://leetcode.com/problems/check-if-n-and-its-double-exist/description/

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        prev = set()
        for num in arr:
            if num / 2 in prev or num * 2 in prev:
                return True
            prev.add(num)
        return False