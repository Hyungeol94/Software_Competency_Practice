#https://leetcode.com/problems/cinema-seat-allocation/description/?envType=daily-question&envId=2026-08-19

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        arr = sorted(reservedSeats)
        total = n
        n = len(arr)
   
        left = 0
        right = 0
        block1 = set([2,3,4,5])
        block2 = set([4,5,6,7])
        block3 = set([6,7,8,9])
        acc = 0 
        acc += (arr[0][0] - 1) * 2
        
        while right < n:
            indices = set()
            while right < n and arr[right][0] == arr[left][0]:
                indices.add(arr[right][1])
                right += 1
            if right < n:
                acc += (arr[right][0] - arr[left][0] - 1)*2
            else:
                acc += (total - arr[left][0])*2
            left = right
            
            if len(indices & block1) == 0:
                if len(indices & block3)== 0:
                    acc += 2
                    
                else:
                    acc += 1
            elif len(indices & block2) == 0:
                    acc += 1
            elif len(indices & block3) == 0:
                acc += 1
        return acc