#https://leetcode.com/problems/implement-router/description/?envType=daily-question&envId=2025-09-20
#3508. Implement Router

from collections import deque
import bisect

class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.packets = deque([])
        self.packets_per_destination = defaultdict(deque)
        self.seen = set()


    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.seen:
            return False
        
        if len(self.packets) == self.memoryLimit:
            packet = self.packets.popleft()
            _, key, _ = packet
            self.packets_per_destination[key].popleft()
            self.seen.remove(packet)

        self.packets.append((source, destination, timestamp))
        self.packets_per_destination[destination].append((source, timestamp))
        self.seen.add((source, destination, timestamp))
        return True
        
        
    def forwardPacket(self) -> List[int]:
        if self.packets: 
            packet = self.packets.popleft()
            _, key, _ = packet
            self.packets_per_destination[key].popleft()
            self.seen.remove(packet)
            return list(packet)
        return []
        

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:      
        arr = self.packets_per_destination[destination]
        start_i = bisect.bisect_left(arr, startTime, key= lambda a: a[1])
        end_i = bisect.bisect_right(arr, endTime, key= lambda a: a[1])
        return end_i-start_i

            

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)