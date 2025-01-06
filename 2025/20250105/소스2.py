#https://leetcode.com/problems/shifting-letters-ii/?envType=daily-question&envId=2025-01-05
#Shifting Letters II

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        acc = [0]*len(s)
        n = len(s)
        for shift in shifts:
            start, end, dr = shift
            if dr == 1:
                acc[start] += 1
                if end < n-1:
                    acc[end+1] -= 1
            
            else:
                acc[start] -= 1
                if end < n-1:
                    acc[end+1] += 1
        
        curr = 0
        arr = [c for c in s]
        for i, c in enumerate(arr):
            curr += acc[i]
            c = chr(
                (ord(c) - ord('a') + curr) % 26 + ord('a')
            )
            arr[i] = c
        
        return "".join(arr)