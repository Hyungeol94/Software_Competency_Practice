#https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/?envType=daily-question&envId=2026-06-28
#1846. Maximum Element After Decreasing and Rearranging

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        #1 이하는 없음
        #1부터 시작해서 올라가기
        sorted_arr = sorted(arr)
        n = len(arr)
        prev = 1
        for i in range(1, n):
            curr = sorted_arr[i]
            if curr - prev <= 1:
                prev = curr
                continue
            curr = prev + 1
            prev = curr
        curr = prev
        return curr