#https://leetcode.com/problems/largest-triangle-area/?envType=daily-question&envId=2025-09-26
#812. Largest Triangle Area

from itertools import combinations
from fractions import Fraction

class Solution:
    def getYIntercept(self, point, inclination) -> float:
        x, y = point
        #y = inclination * x + yIntercept
        yIntercept = y - (inclination * x)
        return yIntercept

    def getHeight(self, points) -> float:
        point1, point2, point3 = points
        a,b = point1
        c,d = point2
        x,y = point3

        if b == d:
            return abs(y-b)
        
        if a == c:
            return abs(x-a)

        # y = ((b-d) / (a-c))*x + ??  <= point1 or point2 대입
        inclination = Fraction((b-d), (a-c))
        yIntercept = self.getYIntercept(point1, inclination)
            
        # y = -(1 / ((b-d)/(a-c)))*x + ?? <= point3 대입
        verticalLineInclination = Fraction(-1, inclination)
        verticalLineYIntercept = self.getYIntercept(point3, verticalLineInclination)

        #inclination * x + yIntercept = verticalLineInclination * x + verticalLineYIntercept
        #( inclination - verticalLineInclination ) * x = (verticalLineYIntercept - yIntercept)
        ##vertical point
        x1 = Fraction((verticalLineYIntercept - yIntercept), (inclination - verticalLineInclination))
        y1 = inclination * x1 + yIntercept
        x2, y2 = points[2]
        height = ((x2-x1)**2 + (y1-y2)**2)**0.5
        return height


    def largestTriangleArea(self, points: List[List[int]]) -> float:
        maxVal = 0
        for combi in combinations(points, 3):
            a, b = combi[0]
            c, d = combi[1]
            width = ((a-c)**2 + (b-d)**2)**0.5
            height = self.getHeight(combi)
            maxVal = max(maxVal, (width*height) / 2 )
        return maxVal