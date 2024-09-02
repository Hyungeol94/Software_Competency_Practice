import bisect
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        curr = 0
        accSum = []
        for i, item in enumerate(chalk):
            curr += item
            accSum.append(curr)
        num =  k % curr #마지막으로 축적된 값으로 나누어, 한번의 iteration으로 찾을 수 있도록 하기
        index = bisect.bisect_left(accSum, num)
        return index if accSum[index] != num else index+1
