class Solution:
    def convert_bin(self, start_bin, goal_bin):
        bin_length = max(len(start_bin), len(goal_bin))
        if len(start_bin) != bin_length:
            start_bin = '0'*(bin_length-len(start_bin)) + start_bin
        if len(goal_bin) != bin_length:
            goal_bin = '0'*(bin_length-len(goal_bin)) + goal_bin
        return ('0b'+start_bin, '0b'+goal_bin)


    def minBitFlips(self, start: int, goal: int) -> int:
        start_bin = bin(start)[2:]
        goal_bin = bin(goal)[2:]
        start_bin, goal_bin = self.convert_bin(start_bin, goal_bin)
        print(start_bin, goal_bin)
        xor = bin(int(start_bin, 2) ^ int(goal_bin, 2))
        return xor[2:].count('1')