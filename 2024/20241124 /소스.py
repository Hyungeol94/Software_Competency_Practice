#https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/description/?envType=daily-question&envId=2024-11-22
#Flip Columns For Maximum Number of Equal Rows

class Solution:
    def countEqualRows(self, row_masks, mask, upper_bound):
        count = 0
        for row_mask in row_masks:
            if row_mask ^ mask == 0 or row_mask ^ mask == upper_bound:
                count += 1
        return count

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        row_masks = []
        for row in matrix:
            row_mask = int('0b'+''.join(list(map(str, row))), 2)
            row_masks.append(row_mask)
        
        maxVal = -float('inf')
        upper_bound = int('0b'+'1'*len(matrix[0]), 2)
        for row_mask in row_masks:
            mask = row_mask
            maxVal = max(maxVal, self.countEqualRows(row_masks, mask, upper_bound))
        return maxVal