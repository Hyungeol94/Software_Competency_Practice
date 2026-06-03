#https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/?envType=daily-question&envId=2026-06-03
#3635. Earliest Finish Time for Land and Water Rides II

from collections import deque

class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """

        n = len(landStartTime)
        m = len(waterStartTime)
        land_slides = [[landStartTime[i], landStartTime[i]+landDuration[i]] for i in range(n)]
        water_slides = [[waterStartTime[i], waterStartTime[i]+waterDuration[i]] for i in range(m)]
                
        #landslide 후 waterslide한다고 가정
        sorted_land_slides = sorted(land_slides, key=lambda a: a[1])
        sorted_water_slides = deque(sorted(water_slides, key=lambda a: a[0]))

        suffix = float('inf')
        suffix_mins = deque([])
        for i in range(m-1, -1, -1):
            suffix = min(suffix, sorted_water_slides[i][1])
            suffix_mins.appendleft(suffix)

        time = float('inf')
        for i in range(n):
            curr = sorted_land_slides[i]
            while sorted_water_slides and sorted_water_slides[0][0] <= curr[1]:
                time = min(time, curr[1] + sorted_water_slides[0][1] - sorted_water_slides[0][0]) # + suffix에서 가장 빠른 endtime
                sorted_water_slides.popleft()
                suffix_mins.popleft()

            if suffix_mins:
                time = min(time, suffix_mins[0])

        #waterslide 후 landslide한다고 가정
        sorted_water_slides = sorted(water_slides, key=lambda a: a[1])
        sorted_land_slides = deque(sorted(land_slides, key=lambda a: a[0]))

        suffix = float('inf')
        suffix_mins = deque([])
        for i in range(n-1, -1, -1):
            suffix = min(suffix, sorted_land_slides[i][1])
            suffix_mins.appendleft(suffix)
        
        for i in range(m):
            curr = sorted_water_slides[i]
            while sorted_land_slides and curr[1] >= sorted_land_slides[0][0]:
                time = min(time, curr[1] + sorted_land_slides[0][1] - sorted_land_slides[0][0],) # + suffix에서 가장 빠른 endtime
                sorted_land_slides.popleft()
                suffix_mins.popleft()
            
            if suffix_mins:
                time = min(time, suffix_mins[0])

        return time