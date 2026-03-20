#https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/?envType=daily-question&envId=2026-03-20
#3567. Minimum Absolute Difference in Sliding Submatrix

from collections import defaultdict
import heapq

class Solution:
    def moveHorizontally(self, grid, start, k):
        m, n = len(grid), len(grid[0])
        diffs = defaultdict(int)
        heap = []
        heapq.heapify(heap)
        ans = []
        
        upper_bound = k**2
        for i in range(upper_bound-1):
            for j in range(i+1, upper_bound):
                num1, num2 = grid[i // k + start][i % k], grid[j // k + start][j % k]
                if num1 == num2:
                    continue
                if num1 > num2:
                    num1, num2 = num2, num1
                diffs[(num2, num1)] += 1
                if diffs[(num2, num1)] == 1:
                    heapq.heappush(heap, (num2-num1, num2, num1))

        ans.append(heap[0][0] if heap else 0)

        #가로 이동
        for j in range(1, n+1-k):
            #없어지는 줄과의 조합 삭제
            #없어지는 줄 => grid[X][j-1]
            for i in range(start, start+k):
                num = grid[i][j-1]
                for u in range(start, start+k):
                    for v in range(j, j+k-1):
                        num1, num2 = num, grid[u][v]
                        if num1 == num2:
                            continue
                        if num1 > num2:
                            num1, num2 = num2, num1
                        diffs[(num2, num1)] -= 1

            #들어오는 줄과의 조합 추가
            #들어오는 줄 => grid[X][j+k-1]
            for i in range(start, start+k):
                num = grid[i][j+k-1]
                for u in range(start, start+k):
                    for v in range(j, j+k-1):
                        num1, num2 = num, grid[u][v]
                        if num1 == num2:
                            continue
                        if num1 > num2:
                            num1, num2 = num2, num1
                        diffs[(num2, num1)] += 1
                        if diffs[(num2, num1)] == 1:
                            heapq.heappush(heap, (num2-num1, num2, num1))
            
            #아래위 비교값 계산
            for i in range(start, start+k-1):
                for u in range(i+1, start+k):
                    #left pop
                    num1, num2 = grid[i][j-1], grid[u][j-1]
                    if num1 == num2:
                        continue
                    if num1 > num2:
                        num1, num2 = num2, num1
                    diffs[(num2, num1)] -= 1

                    #right push
                    num1, num2 = grid[i][j+k-1], grid[u][j+k-1]
                    if num1 == num2:
                        continue
                    if num1 > num2:
                        num1, num2 = num2, num1
                    diffs[(num2, num1)] += 1
                    if diffs[(num2, num1)] == 1:
                        heapq.heappush(heap, (num2-num1, num2, num1))

            while heap:
                _, num2, num1 = heap[0]
                if diffs[(num2, num1)] == 0:
                    heapq.heappop(heap)
                else:
                    break
            
            if heap:
                diff, _, _ = heap[0]
                ans.append(diff)
            else:
                ans.append(0)

        return ans
        
        
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        #tuple에 대한 hash table 유지 (distinct, 정렬 기준은 abs diff)
        #삽입 => heap
        #삭제 => 0이라면, pop하기
        m, n = len(grid), len(grid[0])
        if k == 1:
            return [[0]*(n - k + 1) for _ in range(m - k + 1)]
        ans = []
        for i in range(m - k + 1):
            ans.append(self.moveHorizontally(grid, i, k))

        return ans