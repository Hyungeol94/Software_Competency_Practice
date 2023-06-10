#88. Merge Sorted Array
#Solution to Leetcode problem
#https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index1 = 0
        index2 = 0
        answer = []
        while index1 != m and index2 != n:
            if nums1[index1] < nums2[index2]:
                answer.append(nums1[index1])
                index1 += 1
            else:
                answer.append(nums2[index2])
                index2 += 1 
            

        if index2 <= n-1:
            while index2 <= n-1:
                answer.append(nums2[index2])
                index2 += 1
            

        if index1 <= m-1:
            while index1 <= m-1: 
                answer.append(nums1[index1])
                index1 += 1
            
        for i, num in enumerate(answer):
            nums1[i] = num

            