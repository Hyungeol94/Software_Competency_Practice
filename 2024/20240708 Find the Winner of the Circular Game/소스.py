class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        count = n
        index = 0
        participants = [i for i in range(1, n+1)]
        while count!=1:
            next_index = (index+k-1) % count
            participants.pop(next_index)
            count -= 1 
            index = (next_index) % count
            
        return participants[0]