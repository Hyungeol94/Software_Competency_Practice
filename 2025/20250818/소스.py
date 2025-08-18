#https://leetcode.com/problems/24-game/?envType=daily-question&envId=2025-08-18
#679. 24 Game

from itertools import permutations, product
from fractions import Fraction

class Solution:
    def operate(self, num1: Fraction, num2: Fraction, operator:str) -> Fraction:
        if operator == '+':
            return num1 + num2

        elif operator == '-':
            return num1 - num2
        
        elif operator == '*':
            return num1 * num2
        
        else: 
            return (num1 / num2) if num2 != 0 else (num1 / -1)

    def calculate(self, nums: List[int], operators: List[str], form: int)->int:
        if form == 1:
            left_operand = self.operate(Fraction(nums[0]), Fraction(nums[1]), operators[0])
            right_operand = self.operate(Fraction(nums[2]), Fraction(nums[3]), operators[2])
            return self.operate(left_operand, right_operand, operators[1])

        elif form ==2:
            res1 = self.operate(Fraction(nums[0]), Fraction(nums[1]), operators[0])
            res2 = self.operate(res1, nums[2], operators[1])
            res3 = self.operate(res2, nums[3], operators[2])
            return res3
        
        else:
            res1 = self.operate(Fraction(nums[2]), Fraction(nums[3]), operators[2])
            res2 = self.operate(Fraction(nums[1]), res1, operators[1])
            res3 = self.operate(Fraction(nums[0]), res2, operators[0])
            return res3
            

    def judgePoint24(self, cards: List[int]) -> bool:
        #STEP1
        #순열 구하기
        #24개 경우
        
        #STEP2
        #가능한 트리 구조에 집어넣기

        for nums in permutations(cards, 4):
            for operators in product(['+', '-', '*', '/'], repeat = 3):
                for form in [1,2,3]:
                    res = self.calculate(nums, operators, form)
                    if res == 24:
                        return True
        return False