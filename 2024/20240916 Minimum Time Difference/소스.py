class Solution:
    def convert_time_points(self, time_point: str) -> int:
        hours, minutes = map(int, time_point.split(':'))
        return minutes + hours*60
    
    def findMinDifference(self, timePoints: List[str]) -> int:
        time_points_sorted = sorted([self.convert_time_points(i) for i in timePoints])
        time_points_2nd = [i+60*24 for i in time_points_sorted]
        arr = time_points_sorted + time_points_2nd

        min_val = float('inf')
        for a, b in zip(arr[:-1], arr[1:]):
            min_val = min(abs(a-b), min_val)
        
        return min_val