class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        answer = []
        numSet = set([0])
        for num in nums:
            if num not in numSet:
                numSet.add(num)
            else:
                answer.append(num)

        return answer