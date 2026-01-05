#https://leetcode.com/problems/maximum-matrix-sum/?envType=daily-question&envId=2026-01-05
#1975. Maximum Matrix Sum

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        #두 쌍으로 붙어 있는 것 => 다 바꾸기 => 짝수개 => 그냥 sum        
        #하나만 있을 떄 => 타고타고 넘겨서 제일 작은 숫자로 보내버리기 가능
        count = 0 
        minVal = float('inf')
        acc = 0
        for row in matrix:
            for item in row:
                if item < 0:
                    count += 1
                minVal = min(minVal, abs(item))
                acc += abs(item)

        if count % 2 == 0:
            return acc
        else:
            return acc - (minVal * 2)