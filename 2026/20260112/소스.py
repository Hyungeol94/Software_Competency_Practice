#https://leetcode.com/problems/minimum-time-visiting-all-points/?envType=daily-question&envId=2026-01-12
#1266. Minimum Time Visiting All Points

class Solution:
    def getMinTime(self, point1: List[int], point2: List[int]) -> int:
        #거리는 abs로 계산하기 (뒤집어도 거리는 똑같음)
        distance = abs(point1[0] - point2[0])
        height = abs(point1[1] - point2[1])

        #distance == height => move diagonally
        if distance == height:
            return distance

        #distance < height => move diagnoally + move upward
        elif distance < height:
            return height

        # distance > height => move diagnoally + move horizontally
        else:
            return distance 

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return sum(map(lambda a: self.getMinTime(*a), list(zip(points[:-1], points[1:]))))