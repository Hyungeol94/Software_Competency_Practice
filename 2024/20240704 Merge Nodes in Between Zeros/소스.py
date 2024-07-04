# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sum = 0
        curr = head.next
        answer = None
        tail = None
        while curr:
            if curr.val == 0:
                if not tail:
                    answer = ListNode(sum, None)
                    tail = answer 
                else:
                    tail.next = ListNode(sum, None)
                    tail = tail.next
                sum = 0
            else:
                sum += curr.val
            curr = curr.next
        return answer
                
        