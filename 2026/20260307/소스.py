#https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/?envType=daily-question&envId=2026-03-07
#1888. Minimum Number of Flips to Make the Binary String Alternating

class Solution:
    def shift(self, n, num_1_in_even_index, num_0_in_odd_index, c) -> List[int]:
        num_0_in_even_index = (n - n // 2) - num_1_in_even_index
        num_1_in_odd_index = n // 2 - num_0_in_odd_index
        
        if c == '0':
            num_0_in_even_index -= 1
        else:
            num_1_in_even_index -= 1

        num_1_in_even_index = num_1_in_odd_index
        num_0_in_odd_index = num_0_in_even_index

        if ((n-1) % 2) == 0:
            #even_index가 영향
            if c == '0':
                num_0_in_even_index += 1
            else:
                num_1_in_even_index += 1
        else:
            if c == '0':
                num_0_in_odd_index += 1
            else:
                num_1_in_odd_index += 1

        return [num_1_in_even_index, num_0_in_odd_index]

    def minFlips(self, s: str) -> int:
        n = len(s)
        num_1_in_even_index = 0
        num_0_in_odd_index = 0
   
        for i, c in enumerate(s):
            if i & 1:
                if c == '0':
                    num_0_in_odd_index += 1
            else:
                if c != '0':
                    num_1_in_even_index += 1
        
        
        num_0_in_even_index = (n - n // 2) - num_1_in_even_index
        num_1_in_odd_index = n // 2 - num_0_in_odd_index
        
        minVal = float('inf')
        minVal = min(minVal, abs(num_1_in_even_index - (n - n // 2)) + abs(num_0_in_odd_index - n // 2 ))
        minVal = min(minVal, abs(num_0_in_even_index - (n - n // 2)) + abs(num_1_in_odd_index - n // 2 ))

        for i in range(n):
            num_1_in_even_index, num_0_in_odd_index = self.shift(n, num_1_in_even_index, num_0_in_odd_index, s[i])
            num_0_in_even_index = (n - n // 2) - num_1_in_even_index
            num_1_in_odd_index = n // 2 - num_0_in_odd_index

            #10101 ... 가정
            minVal = min(minVal, abs(num_1_in_even_index - (n - n // 2)) + abs(num_0_in_odd_index - n // 2 ))
            
            #010101 ... 가정
            minVal = min(minVal, abs(num_0_in_even_index - (n - n // 2)) + abs(num_1_in_odd_index - n // 2 ))

        return minVal
