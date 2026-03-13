#https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/description/?envType=daily-question&envId=2026-03-13
#3296. Minimum Number of Seconds to Make Mountain Height Zero
import math

class Solution:
    def getMaxHeight(self, second_bound, workerTime):
        maxHeight = 1
        acc_second = maxHeight * workerTime
        while acc_second <= second_bound:
            maxHeight += 1
            acc_second += maxHeight * workerTime
        return maxHeight - 1


    def is_possible(self, second, mountainHeight, workerTimes):
        if sum(map(
            lambda a: self.getMaxHeight(second, a), 
            workerTimes
        )) >= mountainHeight:
            return True
        return False
              
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        n = len(workerTimes)
        left = 0
        
        #인당 적어도 minHeight만큼은 해야 함
        minHeight = math.ceil(mountainHeight / n)
        #모두 다 동시에 작업한다고 가정했을 때 걸리는 시간
        right = max(workerTimes) * int((minHeight + 1 ) * minHeight / 2)
        minSecond = None
        #False False False True True True ... 이런 식으로 나올 것

        while left <= right:
            mid = (left + right) // 2 
            if self.is_possible(mid, mountainHeight, workerTimes):
                minSecond = mid
                right = mid - 1
            else:
                left = mid + 1
        return minSecond