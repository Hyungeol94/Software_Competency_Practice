# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = None
        curr = head
        indices = []
        index = 1

        while curr.next:
            if not prev:
                prev = curr
                curr = curr.next
                continue

            if not curr.next:
                break
            
            if prev.val < curr.val and curr.next.val < curr.val:
                indices.append(index)
            
            if curr.val < prev.val and curr.val < curr.next.val:
                indices.append(index)
            
            prev = curr
            curr = curr.next
            index += 1
        
        # indices에는 local maxima, local minima들의 인덱스가 있음
        if len(indices) < 2:
            return [-1, -1]
        
        maxDistance = indices[-1]-indices[0]
        minDistance = float('inf')
        for left, right in zip(indices[:-1], indices[1:]):
            minDistance = min(minDistance, abs(right-left))

        return [minDistance, maxDistance]





            
            