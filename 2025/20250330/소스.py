#https://leetcode.com/problems/partition-labels/?envType=daily-question&envId=2025-03-30
#763. Partition Labels

from collections import defaultdict
from collections import deque

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #merge interval
        indices = defaultdict(list)
        for i, c in enumerate(s):
            indices[c].append(i)
        
        arr = []
        for key, elements in indices.items():
            arr.append([elements[0], elements[-1]])
        
        #시작시간 기준으로 정렬하기
        arr.sort(key = lambda a : a[0])

        mystack = []
        for interval in arr:
            if not mystack:
                mystack.append(interval)
                continue
            
            if interval[0] < mystack[-1][1]:
                mystack[-1] = [
                    min(interval[0], mystack[-1][0]),
                    max(interval[1], mystack[-1][1])
                    ]
            else:
                mystack.append(interval)
        
        answer = []
        for interval in mystack:
            distance = interval[1]-interval[0]+1
            answer.append(distance)
        return answer