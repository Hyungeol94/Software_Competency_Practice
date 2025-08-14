#https://leetcode.com/problems/largest-3-same-digit-number-in-string/description/?envType=daily-question&envId=2025-08-14

class Solution:
    def is_good(self, num: str):
        if num[0] == num[1] and num[1] == num[2]:
            return True
        return False

    def largestGoodInteger(self, num: str) -> str:
        maxGood = "-1"
        for i in range(len(num)-2):
            candidate = num[i:i+3]
            if self.is_good(candidate):
                maxGood = str(max(int(maxGood), int(candidate)))
        return ("000" if maxGood == "0" else maxGood) if maxGood != "-1" else ""