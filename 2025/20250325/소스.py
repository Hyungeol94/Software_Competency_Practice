#https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/?envType=daily-question&envId=2025-03-25
#3394. Check if Grid can be Cut into Sections

class Solution:
    def is_possible(self, intervals: int) -> bool:
        mystack = [intervals[0]]
        for interval in intervals:
            top_start, top_end = mystack[-1]
            curr_start, curr_end = interval
            if curr_start < top_end:
                mystack[-1] = [min(top_start, curr_start), max(top_end, curr_end)]
            else:
                mystack.append(interval)
        # print(mystack)
        if 3 <= len(mystack):
            return True
        return False
                
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        #interval 문제
        #세 개의 part로 나눠질 수 있는지 확인

        horizontal_intervals = sorted([[rectangle[0], rectangle[2]] for rectangle in rectangles])
        vertical_intervals = sorted([[rectangle[1], rectangle[3]] for rectangle in rectangles])

        if self.is_possible(horizontal_intervals) or self.is_possible(vertical_intervals):
            return True
        return False