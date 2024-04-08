from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches.reverse()
        while students and sandwiches:
            if students[0] == sandwiches[-1]:
                students.popleft()
                sandwiches.pop()
            else:
                count = 0
                while count!=len(students):
                    students.rotate(-1)
                    count += 1
                    if students[0] == sandwiches[-1]:
                        break
                if count == len(students):
                    return len(students)
        return 0