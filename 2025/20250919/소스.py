#https://leetcode.com/problems/design-spreadsheet/description/?envType=daily-question&envId=2025-09-19
#3484. Design Spreadsheet
import re

class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = [[0 for _ in range(ord('Z')-ord('A')+1)] for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        self.sheet[int(cell[1:])-1][ord(cell[0])-ord('A')] = value

    def resetCell(self, cell: str) -> None:
        self.sheet[int(cell[1:])-1][ord(cell[0])-ord('A')] = 0
        
    def getValue(self, formula: str) -> int:
        elements = [item for item in re.split("[=+]", formula) if item]
        element1, element2 = elements
        value1 = self.sheet[int(element1[1:])-1][ord(element1[0])-ord('A')] if not element1.isnumeric() else int(element1)
        value2 = self.sheet[int(element2[1:])-1][ord(element2[0])-ord('A')] if not element2.isnumeric() else int(element2)
        return value1 + value2

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)