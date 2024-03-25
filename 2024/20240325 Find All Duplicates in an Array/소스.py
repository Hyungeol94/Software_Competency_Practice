class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        answer = []
        check = 0
        for num in nums:
            if not check & (1 << num):
                check = check | (1 << num)
            else:
                answer.append(num)
        return answer