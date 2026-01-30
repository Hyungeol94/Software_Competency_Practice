#https://leetcode.com/problems/roman-to-integer/
#13. Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            'I': 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        romans_with_subtractions = {
            'IV' : 4,    
            'IX' : 9,
            'XL' : 40,
            'XC' : 90,  
            'CD' : 400, 
            'CM' : 900
        }

        acc = 0
        while s:
            is_found = False
            for key, value in romans_with_subtractions.items():
                if not s.startswith(key):
                    continue
                acc += value
                is_found = True
                s = s[2:]
            
            if is_found:
                continue
            
            for key, value in romans.items():
                if not s.startswith(key):
                    continue
                acc += value
                s = s[1:]
        
        return acc