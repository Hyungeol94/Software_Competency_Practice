#https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/?envType=daily-question&envId=2026-03-01
#1689. Partitioning Into Minimum Number Of Deci-Binary Numbers

class Solution:
    def minPartitions(self, n: str) -> int:
        return max(list(map(lambda a: int(a), n)))