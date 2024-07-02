# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr = head
        numNodes = 0
        while curr!= None:
            numNodes += 1
            prev = curr
            curr = curr.next
        
        count = 0
        prev = None
        curr = head
        while curr!=None:
            count += 1
            if count == numNodes-n+1:
                if prev:
                    prev.next = curr.next
                else:
                    head = head.next
                curr = curr.next
                break
            prev = curr
            curr = curr.next
        return head