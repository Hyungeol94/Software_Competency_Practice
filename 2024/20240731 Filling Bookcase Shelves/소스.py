from collections import deque
from copy import copy

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        #이제 dp인 게 이해가 됨!
        @cache
        def dp(i, remaining_width, max_height):
            #선택했을 때
            thickness, height = books[i]
            if i == len(books)-1:
                if thickness <= remaining_width:
                    return max(max_height, height)
                else:
                    return  max_height+height

            if thickness <= remaining_width:
                return min(dp(i+1, remaining_width-thickness, max(max_height, height)), max_height + dp(i+1, shelfWidth-thickness, height))
            
            else:
                return max_height + dp(i+1, shelfWidth-thickness, height)
        
        return dp(0, shelfWidth, books[0][1])