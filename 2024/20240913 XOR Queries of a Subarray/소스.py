class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        acc = []
        for item in arr:
            last = acc[-1] if len(acc) > 0 else 0
            curr = last ^ item
            acc.append(curr)
        print(acc)
        answer = []
        for query in queries:
            start = acc[query[0]-1] if 1 <= query[0] else 0
            end = acc[query[1]]
            answer.append(start^end)
            
        return answer 