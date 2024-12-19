import heapq

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        #정렬 되어 있지 않은 구간을 찾아서 하나의 chunk로 만들기
        #정렬이 되어 있다면 그 구간은 건너뛰기 
        n = len(arr)
        num_chunk = 0

        missing_elements_heap = []
        found_elements_heap = []
        heapq.heapify(missing_elements_heap)
        heapq.heapify(found_elements_heap)

        for i, num in enumerate(arr):
            if i != num:
                heapq.heappush(missing_elements_heap, i)
                heapq.heappush(found_elements_heap, num)
                while missing_elements_heap and missing_elements_heap[0] == found_elements_heap[0]:
                    heapq.heappop(missing_elements_heap)
                    heapq.heappop(found_elements_heap)
                if not missing_elements_heap:
                    num_chunk += 1

            else: #같다는 것을 확인
                if missing_elements_heap: #heap이 남아있다면
                    heapq.heappush(missing_elements_heap, i)
                    heapq.heappush(found_elements_heap, num)

                else:
                    num_chunk += 1
        
        return num_chunk