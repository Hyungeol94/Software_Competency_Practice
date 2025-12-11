#https://leetcode.com/problems/count-covered-buildings/description/?envType=daily-question&envId=2025-12-11
#3531. Count Covered Buildings

from collections import defaultdict

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        #x별로 나누고, y별로 나누고
        min_by_x = defaultdict(lambda: float('inf'))
        max_by_x = defaultdict(lambda: -float('inf'))
        min_by_y = defaultdict(lambda: float('inf'))
        max_by_y = defaultdict(lambda: -float('inf'))

        for x, y in buildings:
            min_by_x[x] = min(min_by_x[x], y)
            max_by_x[x] = max(max_by_x[x], y)
            min_by_y[y] = min(min_by_y[y], x)
            max_by_y[y] = max(max_by_y[y], x)
        
        seen = set()
        seen = seen.union(set(list(map(tuple, min_by_x.items()))))
        seen = seen.union(set(list(map(tuple, max_by_x.items()))))
        seen = seen.union(set(list(map(lambda a: (a[1], a[0]), min_by_y.items()))))
        seen = seen.union(set(list(map(lambda a: (a[1], a[0]), max_by_y.items()))))

        return len(buildings)-len(seen)