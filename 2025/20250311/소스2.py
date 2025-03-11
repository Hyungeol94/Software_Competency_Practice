from collections import defaultdict
from collections import deque

def solution(priorities, location):
    freqDist = defaultdict(int)
    
    for priority in priorities:
        freqDist[priority] += 1
    
    keys = deque(sorted(freqDist.keys(), key=lambda a: -a)) #priority 별로 정렬해두기 
    myqueue = deque([(i, priority) for i, priority in enumerate(priorities)])
    orders = []

    while myqueue:
        i, priority = myqueue.popleft()
        if priority == keys[0]: #가장 먼저 나갈 수 있음
            freqDist[priority] -= 1 
            if freqDist[priority] == 0:
                del freqDist[priority]
                keys.popleft()
            orders.append(i)
        else:
            myqueue.append((i, priority))
            
    return orders.index(location)+1