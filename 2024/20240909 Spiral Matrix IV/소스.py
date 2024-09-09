# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        d_rows = [0, 1, 0, -1]
        d_cols = [1, 0, -1, 0]
        i = 0
        curr = head
        curr_row = 0
        curr_col = 0
        matrix[0][0] = head.val
        curr = head.next
        while curr:
            next_row = curr_row + d_rows[i]
            next_col = curr_col + d_cols[i]
            if not (0 <= next_row < m and 0 <= next_col < n):
                i = (i+1) % 4 
                continue
            if matrix[next_row][next_col] != -1:
                i = (i+1) % 4 
                continue
            matrix[next_row][next_col] = curr.val
            curr = curr.next 
            curr_row = next_row
            curr_col = next_col
        return matrix