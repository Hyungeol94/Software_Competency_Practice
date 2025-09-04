#https://leetcode.com/problems/find-closest-person/description/?envType=daily-question&envId=2025-09-04
#3516. Find Closest Person

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        x_distance = abs(z-x)
        y_distance = abs(z-y)
        if x_distance == y_distance:
            return 0
        
        elif x_distance < y_distance:
            return 1
        
        else:
            return 2