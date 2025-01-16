#https://leetcode.com/problems/minimize-xor/description/?envType=daily-question&envId=2025-01-15
#2429. Minimize XOR
class Solution:
    def convert_to_bins(self, num1, num2):
        num1_bin = bin(num1)[2:]
        num2_bin = bin(num2)[2:]
        maxLen = max(len(num1_bin), len(num2_bin))
        num1_bin = "0"*(maxLen-len(num1_bin)) + num1_bin
        num2_bin = "0"*(maxLen-len(num2_bin)) + num2_bin
        return (num1_bin, num2_bin)


    def minimizeXor(self, num1: int, num2: int) -> int:
        num1_bin, num2_bin = self.convert_to_bins(num1, num2)
        print(num1_bin, num2_bin)
        num1_bits = num1_bin.count("1")
        num2_bits = num2_bin.count("1")

        if num1_bits == num2_bits:
            return num1
        
        arr = []
        if num2_bits < num1_bits:
            #제일 왼쪽에서부터 1을 찾아 지우기 
            diff = num2_bits
            for c in num1_bin:
                if c == "1":
                    if diff:
                        arr.append("1")
                        diff -= 1
                    else:
                        arr.append("0")  
                else:
                    arr.append(c)
            return int('0b'+"".join(arr), 2)
        
        if num2_bits > num1_bits:
            #제일 오른쪽에서부터 0을 찾아 넣기
            diff = num2_bits - num1_bits
            for c in reversed(num1_bin):
                if c == "0" and diff:
                    arr.append("1")
                    diff -= 1 
                    continue
                arr.append(c)
            return int('0b'+"".join(arr[::-1]), 2)