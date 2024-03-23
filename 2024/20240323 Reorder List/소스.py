# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_rightmost_node(self, head):
        lefthand = None
        curr = head
        while curr.next:
            lefthand = curr
            curr = curr.next
        return [lefthand, curr]

    def get_lefthand_node(self, head, right):
        curr = head
        while curr!=None and curr.next != right:
            curr = curr.next
        return curr
        

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        #전체 길이 구하기
        curr = head
        n = 1
        while curr.next:
            curr = curr.next
            n += 1

        i = 1
        state = 0
        leftmost_node = head
        [lefthand_node, rightmost_node] = self.get_rightmost_node(leftmost_node)
        while i<=n:
            [lefthand_node, rightmost_node] = self.get_rightmost_node(leftmost_node)
            temp = leftmost_node.next
            leftmost_node.next = rightmost_node
            leftmost_node = temp

            if i != n-1:
                rightmost_node.next = leftmost_node
                if lefthand_node:
                    lefthand_node.next = None
            i += 2
            # if lefthand_node == left:
            #     rightmost_node.next = None
            

        
        
        
        