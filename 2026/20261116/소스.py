#https://leetcode.com/problems/calculate-digit-sum-of-a-string/description/?envType=daily-question&envId=2026-11-16
#2243. Calculate Digit Sum of a String

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            arr = []
            for i in range(0, len(s), k):
                arr.append(str(sum(list(map(int, s[i:i+k])))))
            
            s = "".join(arr)
        
        return s