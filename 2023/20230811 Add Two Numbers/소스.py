#https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:                
        p1, p2 = l1, l2
        p3 = l3 = ListNode(val = (p1.val+p2.val if p1.val+p2.val<10 else p1.val+p2.val-10))        
        p3.next = ListNode(val = 0 if p1.val+p2.val<10 else 1) if (p1.next or p2.next or not p1.val+p2.val<10) else None
        p3 = p3.next if p3.next else None

        while True:
            if p1.next and p2.next:
                p1 = p1.next
                p2 = p2.next
                p3.next = ListNode(val = 0 if p3.val+p1.val+p2.val<10 else 1) if (p1.next or p2.next or not p3.val+p1.val+p2.val<10) else None
                p3.val = p3.val+p1.val+p2.val if p3.val+p1.val+p2.val<10 else p3.val+p1.val+p2.val-10   
                p3 = p3.next if p3.next else None
                
            elif p1.next and not p2.next:
                p1 = p1.next
                p3.next = ListNode(val=0 if p3.val+p1.val<10 else 1) if (p1.next or p2.next or not p3.val+p1.val<10) else None        
                p3.val = p3.val+p1.val if p3.val+p1.val<10 else p3.val+p1.val-10
                p3 = p3.next if (p1.next or p2.next) else None               
                
            elif not p1.next and p2.next:
                p2 = p2.next
                p3.next = ListNode(val =0 if p3.val+p2.val<10 else 1) if (p1.next or p2.next or not p3.val+p2.val<10) else None         
                p3.val = p3.val+p2.val if p3.val+p2.val<10 else p3.val+p2.val-10   
                p3 = p3.next if p3.next else None
            
            elif not p1.next and not p2.next:
                break

        return l3


            
            
            
            


            


            

            
            
        