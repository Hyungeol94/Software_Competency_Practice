# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        #링크드 리스트의 길이 구하기
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        (size, extra) = divmod(length, k)
        parts_length = [size]*k
        answer = []
        prev = None
        curr = head
        for i, _ in enumerate(parts_length):
            if i < extra:
                parts_length[i] += 1
            
            size = parts_length[i]
            count = 0
            start = curr
            while count != size:
                prev = curr
                curr = curr.next
                count += 1
            if prev:
                prev.next = None
            
            answer.append(start)
            #바로 끊는거 진행하기
        return answer