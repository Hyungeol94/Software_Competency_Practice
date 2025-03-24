#https://leetcode.com/problems/count-days-without-meetings/?envType=daily-question&envId=2025-03-24
#3169. Count Days Without Meetings

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        #interval 문제
        #merge interval
        #시작 시간으로 정렬
        #겹치면 merge하기

        sorted_meetings = sorted(meetings)
        mystack = [sorted_meetings[0]]
        for meeting in sorted_meetings:
            top_start, top_end = mystack[-1]
            meeting_start, meeting_end = meeting
            if meeting_start <= top_end:
                mystack[-1] = [min(top_start, meeting_start), max(top_end, meeting_end)]
            else:
                mystack.append(meeting)
        
        available_days = days
        for schedule in mystack:
            available_days -= (schedule[1]-schedule[0] + 1 )
        return available_days
