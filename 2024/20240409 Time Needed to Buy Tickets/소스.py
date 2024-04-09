#https://leetcode.com/problems/time-needed-to-buy-tickets/

from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        tickets = deque(tickets)
        n = len(tickets)
        i = 0
        while tickets[(k-i) % n]!=0:
            if tickets[0]!=0:
                tickets[0] -= 1
                count += 1
            i += 1
            tickets.rotate(-1)
        return count

            