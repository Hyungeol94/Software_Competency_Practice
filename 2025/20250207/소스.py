#https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/?envType=daily-question&envId=2025-02-07
#3160. Find the Number of Distinct Colors Among the Balls

from collections import defaultdict

class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        arr = defaultdict(int)
        colorFreq = defaultdict(int)

        count = 0
        answer = []
        for query in queries:
            index, newColor = query
            oldColor = arr[index]
            #동일함
            if oldColor == newColor: 
                answer.append(count)
                continue
            
            #동일하지 않음
            if colorFreq[oldColor] == 1: #유일한 색
                if 1 <= colorFreq[newColor]: #유일하지 않은 색
                    count -= 1 
               
            elif 1 < colorFreq[oldColor] or arr[index] == 0: #유일하지 않은 색
                if colorFreq[newColor] == 0: #유일한 색
                    count += 1

            colorFreq[oldColor] -= 1
            colorFreq[newColor] += 1
            arr[index] = newColor
            answer.append(count)
        
        return answer