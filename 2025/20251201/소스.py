#https://leetcode.com/problems/maximum-running-time-of-n-computers/?envType=daily-question&envId=2025-12-01
#2141. Maximum Running Time of N Computers

from collections import Counter

class Solution:
    def isPossible(self, n, batteries, k):
        #determine if it is possible to run all n computers simultaneously in a given miutes
        if len(batteries) == n:
            return True if min(batteries) >= k else False
        
        if sum(batteries) < n * k:
            return False

        #교체해가면서 넣어야 하는 상황
        counter = sorted(Counter(batteries).items(), key= lambda a: -a[0])

        #X (방법1) 정렬된 배열의 앞에 있는 n개의 배터리의 분 수를 다 1씩 줄이기 => 재정렬 => K번 반복할 수 있는가?
        #O (방법2) k 이상의 배터리 양을 가진 n개의 배터리를 (조합해서) 만들 수 있는가?
        
        count = 0
        for i, [cap, num] in enumerate(counter):
            if count >= n:
                return True
            if cap >= k:
                count += num
            if cap < k:
                #일단 끊기
                break

        #몇개를 더 채워야 할까? => n-count개를 더 채워야 함 => target 개라고 가정
        #i 이하의 인덱스를 기준으로, 여러 배터리를 조합해서 k 이상인 배터리 target개를 만들 수 있을까?
        counter = counter[i:]
        target = n-count
        
        
        #sum했을 때 target * k 이상이어야 함
        #남은 개수가 target개보다 많이 남아 있어야 함 => 조합해야 하니까 더 많이 있어야 할듯 
        #k를 넘지 않는 cap을 가진 배터리 여러개를 합친 값 >= target * k라면? 무조건 count >= target이다
        count = 0
        acc = 0

        for i, [cap, num] in enumerate(counter):
            count += num
            acc += cap * num

        
        if acc >= target * k:
                return True
        
        return False
        
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left = 0
        right = sum(batteries) // n 
        maxNum = 0
        while left <= right:
            mid = (left + right) // 2 
            if self.isPossible(n, batteries, mid):
                maxNum = max(maxNum, mid)
                left = mid+1
            else:
                right = mid-1
        return maxNum