#https://school.programmers.co.kr/learn/courses/30/lessons/120956

import re

class pronouncableWordCount:
    def __init__(self, babbling):
        self.babbling = babbling
        self.pronouncableUnits = ["aya", "ye", "woo", "ma"]

    def deleteThisUnit(self, unit):
        self.babbling = [self.deleteThisUnitCallback(word, unit) for word in self.babbling]


    def deleteThisUnitCallback(self, word, unit):
        return re.sub(unit, '.', word)

    def getPronouncableWordCount(self):
        for i, unit in enumerate(self.pronouncableUnits):
            self.deleteThisUnit(unit)

        return sum(1 for word in self.babbling if re.match('^[.]*$', word))


def solution(babbling):
    solutionInstance = pronouncableWordCount(babbling)
    return solutionInstance.getPronouncableWordCount()
