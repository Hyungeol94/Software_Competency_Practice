from collections import defaultdict
import heapq

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        char_dict = defaultdict(int)
        for c in s:
            char_dict[c] += 1
        
        heap = []
        heapq.heapify(heap)

        for key, value in char_dict.items():
            heapq.heappush(heap, [-ord(key), value, key])
        
        answer = ""
        while heap:
            curr = heapq.heappop(heap)
            _, value, char = curr
            if answer and char == answer[-1]:
                break

            if value <= repeatLimit:
                answer += char * value
                continue
            
            tweaked_data = [-ord(char), value-repeatLimit, char]

            answer += char * repeatLimit
            if heap:
                curr = heapq.heappop(heap)
                _, value, char = curr
                answer += char
                if 0 < value-1:
                    heapq.heappush(heap, [-ord(char), value-1, char])
                heapq.heappush(heap, tweaked_data)
            else:
                break

        return answer