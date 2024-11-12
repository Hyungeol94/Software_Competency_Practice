class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        memo = {}
        sorted_queries = sorted(queries)
        sorted_items = sorted(items, key=lambda a: (a[0], -a[1]))
        
        index = 0
        maxVal = -float('inf')
        for query in sorted_queries:
            price_limit = query
            curr = sorted_items[index]
            price, beauty = curr
            while price <= price_limit: ##price, beauty
                maxVal = max(maxVal, beauty)
                if index == len(sorted_items)-1:
                    break
                else:
                    index += 1
                price, beauty = sorted_items[index]
            memo[query] = maxVal if maxVal != -float('inf') else 0
        
        answer = []
        for query in queries:
            answer.append(memo[query])
        return answer