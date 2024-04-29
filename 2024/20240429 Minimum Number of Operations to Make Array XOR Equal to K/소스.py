from functools import reduce

class Solution:
    def getBinNums(self, k, v):
        binNumV = bin(k)[2:]
        binNumK = bin(v)[2:]
        if len(binNumV) == len(binNumK):
            return [binNumV, binNumK]
        
        if len(binNumV) > len(binNumK):
            while len(binNumV) != len(binNumK):
                binNumK = '0'+binNumK
        
        else:
            while len(binNumV) != len(binNumK):
                binNumV = '0'+binNumV
        
        return [binNumV, binNumK]

    def minOperations(self, nums: List[int], k: int) -> int:        
        xor = reduce(lambda x, y: x^y, nums)
        binNumK, binNumXor = self.getBinNums(k, xor)
        count = 0
        for c1, c2 in zip(binNumK, binNumXor):
            if c1!=c2:
                count += 1
        
        return count
