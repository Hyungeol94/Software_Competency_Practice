https://leetcode.com/problems/crawler-log-folder/?envType=daily-question&envId=2024-07-10

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        curr = 0
        for log in logs:
            if log == "../":
                if curr == 0:
                    continue
                curr -= 1
                continue
            if log == './':
                continue
            else:
                curr += 1
        return curr