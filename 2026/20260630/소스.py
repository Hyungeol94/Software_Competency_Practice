#https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/?envType=daily-question&envId=2026-06-30
#1358. Number of Substrings Containing All Three Characters

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        #O(n^2) worst-case 2억5천번
        #O(n) postfix first occurence를 구하기
        #memory 저장 => 5만

        a_postfixes = [] 
        b_postfixes = []
        c_postfixes = []
        a_postfix = float('inf')
        b_postfix = float('inf')
        c_postfix = float('inf')

        n = len(s)
        for i in range(n-1, -1, -1):
            c = s[i]
            if c =='a':
                a_postfix = i
            elif c == 'b':
                b_postfix = i
            else:
                c_postfix = i
            a_postfixes.append(a_postfix)
            b_postfixes.append(b_postfix)
            c_postfixes.append(c_postfix)
        
        a_postfixes = a_postfixes[::-1]
        b_postfixes = b_postfixes[::-1]
        c_postfixes = c_postfixes[::-1]

        count = 0
        for i in range(n):
            sub_str_index = max(a_postfixes[i], b_postfixes[i], c_postfixes[i])
            if sub_str_index == float('inf'):
                break
            count += n - sub_str_index 
        return count
