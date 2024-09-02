class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []
        
        answer = []
        i = 0
        limit = (len(original) // n)
        while i!= limit*n:
            answer.append(original[i:i+n])
            i+= n
        return answer
