#https://leetcode.com/problems/minimum-penalty-for-a-shop/?envType=daily-question&envId=2025-12-26
#2483. Minimum Penalty for a Shop

from collections import deque

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        #구하고자 하는 것
        #penalty의 최솟값
        #i까지 열어놨을 때의 penalty

        #필요한 것
        #prefix count of customers not visitied
        #postfix count of customers visited

        prefixes = []
        n = len(customers)
        count = 0
        prefixes.append(0)
        for customer in customers:
            if customer == "N":
                count += 1
            prefixes.append(count)
        
        postfixes = deque([])
        count = 0
        postfixes.appendleft(0)
        for customer in reversed(customers):
            if customer == "Y":
                count += 1
            postfixes.appendleft(count)

        
        answer = 0
        minVal = float('inf')
        for i, [prefix, postfix] in enumerate(zip(prefixes, postfixes)):
            if prefix + postfix < minVal:
                minVal = prefix + postfix
                answer = i

        return answer