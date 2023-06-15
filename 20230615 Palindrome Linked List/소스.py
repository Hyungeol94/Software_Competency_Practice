#https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next\

import copy
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        num_list = []
        num_list.append(head.val)
        next = head.next        
        while next:
            num_list.append(next.val)
            next = next.next
        
        if len(num_list)%2!=0:            
            num_list.pop(len(num_list)//2)
        
        buffer = copy.deepcopy(num_list)
        for i in range(len(num_list)//2):
           if num_list[i]==num_list[-1-i]:
               buffer.pop(0)
               buffer.pop(-1)
        if buffer:
            return False
        else:
            return True