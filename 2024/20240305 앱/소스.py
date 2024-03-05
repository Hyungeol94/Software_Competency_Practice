#https://www.acmicpc.net/problem/7579


from functools import lru_cache
class Solution():
    def minCost(self, n, k, memories, costs):
        #메모리 크기별로 정렬하기
        arr = list(zip(memories, costs)).sort(key=lambda a: a[0])
        #sliding window 방식
        if n == 1:
            return costs[0]

        left = 0
        right = 1
        sum = memories[0]+memories[1]
        cost = costs[0]+costs[1]
        minCost = float('inf')
        while left!=n-1:
            if sum < k:
                right = right+1 if right!=n-1 else right
                sum = sum+memories[right] if right!=n-1 else sum
                cost = cost + costs[right] if right != n - 1 else cost
            else:
                minCost = min(minCost, cost)
                sum = sum - memories[left] if (left!=n-1 and left < right) else sum
                cost = cost - costs[left] if (left!=n-1 and left < right) else cost
                left = left+1 if (left!=n-1 and left < right) else left

            if right == n-1:
                while True:
                    if k <= sum and left<=n-1:
                        minCost = min(minCost, cost)
                        sum = sum - memories[left]
                        cost = cost - costs[left]
                    else:
                        left = n-1
                        break


        return minCost



instance = Solution()
n, k = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))
print(instance.minCost(n, k, memories, costs))