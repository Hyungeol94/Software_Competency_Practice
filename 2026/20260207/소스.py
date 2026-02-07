#https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/?envType=daily-question&envId=2026-02-07
#1653. Minimum Deletions to Make String Balanced

class Solution:
    def minimumDeletions(self, s: str) -> int:
        #왼쪽에는 a만 있고 오른쪽에는 b만 있는 상태
        #b_prefix_count가 0이고, a_suffix_count가 0인 상태

        #각각 구하기
        #b_prefix_count
        #a_suffix_count
        n = len(s)

        b_acc = 0
        b_prefix_count = [0]
        for c in s:
            if c == 'b':
                b_acc += 1
            b_prefix_count.append(b_acc)
    

        a_acc = 0
        a_suffix_count = []
        for c in reversed(s):
            if c == 'a':
                a_acc += 1
            a_suffix_count.append(a_acc)
        
        a_suffix_count = a_suffix_count[::-1]
        a_suffix_count.append(0)

        minVal = float('inf')
        for i in range(n):
            minVal = min(minVal, a_suffix_count[i+1]+b_prefix_count[i])
        
        return minVal