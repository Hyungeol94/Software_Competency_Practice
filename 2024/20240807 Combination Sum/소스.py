from copy import deepcopy 
class Solution:
    def __init__(self):
            self.mystack = []
            self.answer = []

    def dfs(self, maxSize, index, depth, currSum, target, candidates):
        if depth == maxSize:
            if currSum == target:
                self.answer.append(deepcopy(self.mystack))
            
        else:
            for i in range(index, len(candidates)):
                if currSum + candidates[i] <= target:
                    self.mystack.append(candidates[i])
                    self.dfs(maxSize, i, depth+1, currSum+candidates[i], target, candidates)
                    self.mystack.pop()


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        for i in range(target // candidates[0] +1 ):
            self.mystack = []
            if self.dfs(i, 0, 0, 0, target, candidates):
                answer.append(self.mystack)
        
        return self.answer