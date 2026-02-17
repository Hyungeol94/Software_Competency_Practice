#https://leetcode.com/problems/rectangle-area-ii/description/
#850. Rectangle Area II

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        #좌표 압축
        points = set()

        for rectangle in rectangles:
            points |= set(rectangle)
        
        point_map = {point:i for i, point in enumerate(sorted(list(points)))}
        n = len(point_map)

        dp = [[0 for _ in range(n)] for _ in range(n)]
        for rectangle in rectangles:
            x1, y1, x2, y2 = list(map(lambda a: point_map[a], rectangle))
            for x in range(x1, x2):
                for y in range(y1, y2):
                    dp[x][y] = 1

        point_map = {i:point for i, point in enumerate(sorted(list(points)))}
        area = 0
        for x in range(n):
            for y in range(n):
                if not dp[x][y]:
                    continue
                x_length = point_map[x+1]-point_map[x]
                y_length = point_map[y+1]-point_map[y]
                area += x_length * y_length
        
        return area % mod
                