# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        i = 0
        currentNode = list1
        while i != a-1:
            currentNode = currentNode.next
            i += 1
        
        j = i
        removedNode = currentNode.next
        while j != b:
            removedNode = removedNode.next
            j += 1

        currentNode.next = list2
        j = 1
        while currentNode.next:
            currentNode = currentNode.next
            j += 1

        currentNode.next = removedNode
        return list1
    
        
    




        
        