#https://leetcode.com/problems/final-value-of-variable-after-performing-operations/?envType=daily-question&envId=2025-10-20
#2011. Final Value of Variable After Performing Operations

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        acc = 0
        for operation in operations:
            if operation.startswith("--") or operation.endswith("--"):
                acc -= 1
            else:
                acc += 1
        return acc