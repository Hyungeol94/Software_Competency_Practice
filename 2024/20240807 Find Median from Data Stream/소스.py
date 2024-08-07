import heapq
import bisect

class MedianFinder:
    def __init__(self):
        self.arr = []
        
    def addNum(self, num: int) -> None:
        index = bisect.bisect_left(self.arr, num)
        self.arr.insert(index, num)

    def findMedian(self) -> float:
        if len(self.arr) == 0:
            return None

        index = len(self.arr) // 2 
        if len(self.arr) % 2 == 0:
            return (self.arr[index-1] + self.arr[index]) / 2
        
        else:
            return self.arr[index]
            

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()