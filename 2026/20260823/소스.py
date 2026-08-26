#https://leetcode.com/problems/sum-game/?envType=daily-question&envId=2026-08-23
#1927. Sum Game

class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        leftSum, rightSum = 0, 0
        leftCount, rightCount = 0, 0
        for i in range(n//2):
            if num[i] != '?':
                leftSum += int(num[i])
            else:
                leftCount += 1

        for i in range(n//2, n):
            if num[i] != '?':
                rightSum += int(num[i])
            else:
                rightCount += 1
        
        if leftSum > rightSum and leftCount >= rightCount:
            return True
        
        if leftSum < rightSum and leftCount <= rightCount:
            return True
        
        if leftSum <= rightSum and leftCount > rightCount:
            leftSum, rightSum = rightSum, leftSum
            leftCount, rightCount = rightCount, leftCount
        
        #이제 무조건 leftSum >= rightSum, leftCount < rightCount임
        count = rightCount - leftCount
        diff = leftSum - rightSum

        div, mod = divmod(count , 2)
        if (div) * 9 > diff:
            return True

        diff -= (div) * 9
        count = mod

        #차이가 안날 때
        if diff == 0:
            if mod:
                return True
            else:
                return False

        #차이가 나면 무조건 앨리스가 이김    
        else: 
            return True