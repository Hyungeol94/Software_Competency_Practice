from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        inDegrees = defaultdict(int)
        for i in range(numCourses):
            inDegrees[i] = 0
            adjList[i] = []

        for a, b in prerequisites:
            adjList[b].append(a)
            inDegrees[a]+= 1
        
        if not prerequisites:
            return [i for i in range(numCourses)]

        myqueue = []
        while inDegrees:
            current_course, num = sorted(inDegrees.items(), key= lambda a: a[1])[0]
            if num!=0:
                return []

            myqueue.append(current_course)
            if current_course in adjList:
                for next_course in adjList[current_course]:
                    inDegrees[next_course] -= 1
            del inDegrees[current_course]
        
        return myqueue if myqueue else [i for i in range(numCourses)]