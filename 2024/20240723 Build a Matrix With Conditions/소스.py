from collections import deque

class Solution:
    def getNumsByConditions(self, k, conditions):
        indegrees = {i:0 for i in range(1, k+1)}
        adjList = [[] for _ in range(k+1)]
        for condition in conditions:
            depart, dest = condition
            indegrees[dest] += 1
            adjList[depart].append(dest)

        nums = []
        myqueue = deque(sorted(list(indegrees.items()), key = lambda a: a[1]))
        while myqueue:
            num, degree = myqueue.popleft()
            arr = [num]
            if degree != 0:
                return []
            del indegrees[num]
            nodes = adjList[num]
            for key in nodes:
                indegrees[key] -= 1

            while myqueue and myqueue[0][1] == degree:
                num, _ = myqueue.popleft()
                arr.append(num)
                del indegrees[num]
                nodes = adjList[num]
                for key in nodes:
                    indegrees[key] -= 1
            
            nums.append(arr)
            myqueue = deque(sorted(list(indegrees.items()), key = lambda a: a[1]))
            
        return nums

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        numsByRowConditions = self.getNumsByConditions(k, rowConditions)
        numsByColConditions = self.getNumsByConditions(k, colConditions)
        arr = []
        for items in numsByColConditions:
            for item in items:
                arr.append(item)
        numsByColConditions = arr
        if not numsByRowConditions or not numsByColConditions:
            return []
        colPositions = {num: i for i, num in enumerate(numsByColConditions)}
        matrix = [[0]*k for _ in range(k)]
        i = 0
        for items in numsByRowConditions:
            if len(items) == 1:
                num = items[0]         
                colPosition = colPositions[num]
                matrix[i][colPosition] = num
                i += 1
                continue
            else:
                items = sorted(items, key = lambda a: colPositions[a])
                for num in items:
                    colPosition = colPositions[num]
                    matrix[i][colPosition] = num
                    i += 1
        return matrix