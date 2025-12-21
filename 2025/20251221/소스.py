#https://leetcode.com/problems/delete-columns-to-make-sorted-ii/editorial/?envType=daily-question&envId=2025-12-21
#955. Delete Columns to Make Sorted II

from collections import defaultdict
from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        n = len(strs)
        m = len(strs[0])
        to_delete = [False for _ in range(m)]

        mystack = ["" for _ in range(n)]
        for k in range(m):
            #키별로 분류
            mydict = defaultdict(list)
            for i in range(n):
                key = mystack[i]
                mydict[key].append(strs[i][k])
            
            #키 내부에서 정렬 확인 
            is_sorted = True
            for key, arr in mydict.items():
                if len(arr) == 1:
                    continue
                prev = "a"
                for i in range(len(arr)):
                    c = arr[i]
                    if ord(prev) > ord(c):
                        is_sorted = False
                        break
                    prev = c
            
            if not is_sorted:
                to_delete[k] = True
                continue
            
            #키 업데이트
            for i in range(n):
                mystack[i] = mystack[i]+strs[i][k]

        return to_delete.count(True)