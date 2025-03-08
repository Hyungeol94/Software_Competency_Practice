#https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/?envType=daily-question&envId=2025-03-08
#2379. Minimum Recolors to Get K Consecutive Black Blocks

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        #투 포인터 방법
        left = 0
        right = 0
        n = len(blocks)

        count = 0
        operations = 0
        minVal = float('inf')

        while right < n:
            while count != k: #count가 같아질 때까지
                operations = operations + 1 if blocks[right] == 'W' else operations 
                right += 1
                count += 1

            minVal = min(minVal, operations)
            operations = operations - 1 if blocks[left] == 'W' else operations
            count -= 1
            left += 1
          
        return minVal