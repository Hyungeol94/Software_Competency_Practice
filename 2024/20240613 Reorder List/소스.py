# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numNodes(self, head):
        count = 1
        temp = head
        while (temp != None and temp.next != None):
            count += 1
            temp = temp.next
        return count

    def reverseListAfterMiddle(self, head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def mergeLists(self, list1, list2):
        p1 = list1
        p2 = list2

        while p1!= None and p2!=None:          
            temp1 = p1.next
            temp2 = p2.next
            p1.next = p2
            p2.next = temp1
            p1 = temp1
            p2 = temp2
        

    def reorderList(self, head: Optional[ListNode]) -> None:
        numNodes = self.numNodes(head)
        count = 0
        
        #가운데 pointer 찾기
        pointer = head
        prev = None
        while count != numNodes // 2 + numNodes % 2:
            prev = pointer
            pointer = pointer.next
            count += 1
        prev.next = None
        
        reversedListAfterMiddle = self.reverseListAfterMiddle(pointer)
        self.mergeLists(head, reversedListAfterMiddle)