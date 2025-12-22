#https://leetcode.com/problems/delete-columns-to-make-sorted-iii/?envType=daily-question&envId=2025-12-22
#960. Delete Columns to Make Sorted III

from functools import cache

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        
        @cache
        def dp(k, prev):
            #현재 index 삭제
            res1 = (1 + dp(k+1, prev)) if k != m-1 else 1

            #현재 index 보존 
            res2 = float('inf')
            if prev != -1:
                #보존이 가능한지 확인
                is_sorted = True
                for i in range(n):
                    if ord(strs[i][k]) < ord(strs[i][prev]): #k는 삭제를 해야하는 index임 => 보존 불가
                        is_sorted = False
                        break
                
                if is_sorted:
                    res2 = dp(k+1, k) if k != m-1 else 0

            else:
                res2 = dp(k+1, k) if k != m-1 else 0
            
            return min(res1, res2)
            
        return dp(0, -1)
            