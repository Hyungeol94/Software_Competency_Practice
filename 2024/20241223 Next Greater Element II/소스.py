import heapq
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        arr = nums + nums
        heap = []
        heapq.heapify(heap)
        ans = []
        n = len(nums)
        for i, num in reversed(list(enumerate(nums))):
            heapq.heappush(heap, i+n)
        
        for i, num in reversed(list(enumerate(nums))):
            while heap and nums[heap[0] % n] <= num:
                heapq.heappop(heap)
            if heap:
                ans.append(nums[heap[0] % n])
            else:
                ans.append(-1)
            heapq.heappush(heap, i)
        return list(reversed(ans))
    

# 오른쪽에서 왼쪽으로 인덱스 값을 가지고 monotonic stack을 관리함 (increasing order로 정렬)
# monotonic stack을 통해 현재의 인덱스와 가까운 인덱스 순으로 탐색할 수 있음

# - 더 큰 곳으로만 갈 수 있기 때문에 작으면 pop
# - 마지막에는 현재의 인덱스도 넣기
# - 다 팝이 되더라도, 현재의 인덱스를 마지막에 넣어줌 -> 왼쪽에 위치한 원소에서 보면 현재 인덱스가 제일 크면서 동시에 제일 가까이 있는 값이 됨