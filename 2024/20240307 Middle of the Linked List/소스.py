#https://leetcode.com/problems/middle-of-the-linked-list/?envType=daily-question&envId=2024-03-07
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        start = head

        while head.next:
            count += 1
            head = head.next

        if count == 1:
            return head
        
        i = 0
        head = start
        limit = (count //2) if (count % 2 == 0) else (count //2)+1
        while i!= limit:
            i += 1
            head = head.next
        return head
 







        