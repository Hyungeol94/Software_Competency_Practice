class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return list(zip(*sorted(zip(heights, names), key= lambda a: -a[0])))[1]