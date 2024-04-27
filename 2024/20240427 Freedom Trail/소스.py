from collections import deque
import copy
from functools import cache

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        @cache
        def dp(i, number):
            #모든 가능한 상황을 구하기
            #그 상황 중에서 제일 적게 들었던 step 수를 더하기
            # current_ring = copy.deepcopy(deque(ring))
            # current_ring.rotate(number)
            current_index = number
            current_index %= len(ring)
            #동일할 때
            # if key[i] == current_ring[0]:
            if key[i] == ring[current_index]:
                if i == len(key)-1:
                    return 1
                else:
                    return 1+dp(i+1, number)
            
            #동일하지 않을 때
            minCount = float('inf')
            steps = 0
            candidates = []
            for count in range(1, math.ceil(len(ring)/2)):
                # current_ring.rotate(1)
                # if key[i] == current_ring[0]:
                current_index += 1
                current_index %= len(ring)
                if key[i] == ring[current_index]:
                    candidates.append([count, count])
                        
            # current_ring = copy.deepcopy(deque(ring))
            # current_ring.rotate(number)
            current_index = number
            count = 0
            for _ in range(math.floor(len(ring)/2), len(ring)):
                # current_ring.rotate(-1)
                current_index -= 1
                current_index %= len(ring)
                count += 1
                # if key[i] == current_ring[0]:
                if key[i] == ring[current_index]:
                    candidates.append([count, -count])
            
            if i == len(key)-1:
                #찍어야 하기 때문에 1을 더함!
                return min(list(zip(*candidates))[0])+1
            else:
                minVal = float('inf')
                for candidate in candidates:
                    minCount, steps = candidate
                    minVal = min(minVal, 1+minCount+dp(i+1, number+steps))
                return minVal
            
        return dp(0, 0)
                
                
                    