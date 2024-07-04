# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        myqueue = []
        heapq.heapify(myqueue)
        for i, ith_list in enumerate(lists):
            if ith_list:
                heapq.heappush(myqueue, [ith_list.val, i])
        
        head = None
        if not myqueue:
            return head

        (_, i) = heapq.heappop(myqueue)
        head = lists[i]
        lists[i] = lists[i].next
        if lists[i]:
                heapq.heappush(myqueue, [lists[i].val, i])
        curr = head

        while myqueue:
            (val, i) = heapq.heappop(myqueue)
            curr.next = lists[i]
            curr = lists[i]
            lists[i] = lists[i].next
            
            if lists[i]:
                heapq.heappush(myqueue, [lists[i].val, i])
        
        return head