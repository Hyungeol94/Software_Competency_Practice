#https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/?envType=daily-question&envId=2025-09-06
#3495. Minimum Operations to Make Array Elements Zero

class Solution:
    def count(self, n)->int:
        i = 0 
        while n != 0:
            n = n // 4
            i += 1
        return i
    
    def reverse(self, n)->int:
        # 1 -> 1 (3개)
        # 2 -> 4 (12개) 15-3 = 12
        # 3 -> 16  63-15 = 48
        # 4 -> 64 255-63 = 192
        if n == 0:
            return 0
        return 4 ** (n-1)
    

    def minOperations(self, queries: List[List[int]]) -> int:
        #각 쿼리에 O(logn) 이상 소요되지 않게 하기
        ans = 0
        for query in queries:
            l, r = query
            l_count = self.count(l)
            r_count = self.count(r)
            
            total = 0
            if l_count == r_count:
                total += (r-l+1) * l_count

            else:
                l_bound = self.reverse(l_count)
                r_bound = self.reverse(r_count)

                for i in range(l_count, r_count):
                    total += (3 * 4**(i-1)) * i
            
                total -= (l-l_bound)*l_count
                total += (r-r_bound+1)*r_count

            ans += ceil(total / 2)
        
        return ans