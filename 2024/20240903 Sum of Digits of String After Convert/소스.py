class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num_string = ''
        for c in s: #각 문자에 대한 연산을 수행해서 num_string을 구성한다
            num_string += str(ord(c)-ord('a')+1)
        
        i = k
        while i != 0:
            num_sum = 0
            for num in num_string:
                num_sum += int(num)
            num_string = str(num_sum)
            i -= 1

        return num_sum 