#3578. Count Partitions With Max-Min Difference at Most K
#https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/description/?envType=daily-question&envId=2025-12-06
#TLE

from collections import deque
import bisect

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return 1
        
        left = 0
        right = 1
        myqueue = deque([])
        
        ranges = [i for i in range(n)]
        myqueue.append(nums[0])
        while left < n:
            if not myqueue:
                myqueue.append(nums[left])
            #하나는 들어가 있는 상태
            right = max(right, left+1)
            while right < n:
                if nums[right] < myqueue[0]:
                    if abs(nums[right] - myqueue[-1]) <= k:
                        myqueue.appendleft(nums[right])
                    else:
                        break
                elif nums[right] > myqueue[-1]: 
                    if nums[right] - myqueue[0] <= k:
                        myqueue.append(nums[right])
                    else:
                        break
                else:
                    #중간에 삽입할 때는 bisect_left와 insert를 사용 (bisect로 인덱스 찾기, insert를 통해 삽입하기)
                    index = bisect.bisect_left(myqueue, nums[right])
                    myqueue.insert(index, nums[right])
                right += 1
            ranges[left] = right-1
            
            #left를 하나씩 올리기
            myqueue.remove(nums[left]) #반드시 있음
            left += 1

        @cache
        def dp(i): #i에서 n-1까지를 partition할 수 있는 방법의 수
            if i == n-1:
                return 1
            
            else:
                count = 0
                upper_bound = ranges[i]
                for j in range(i, n):
                    if j > upper_bound:
                        break
                    count += dp(min(j+1, n-1)) % (10 ** 9 + 7)
                return count % (10 ** 9 + 7)


        return dp(0)