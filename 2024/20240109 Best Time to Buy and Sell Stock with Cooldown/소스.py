from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        sellingPoint = -1
        sumProfit = 0
        currentProfit = 0
        while right < len(prices):
            if currentProfit < prices[right] - prices[left]:
                currentProfit = prices[right] - prices[left]
                right += 1
                if right == len(prices):
                    sumProfit += currentProfit
                continue
            else:
                # detect peak -> calculate if cooldown is worth it
                if (0 <= right - 2) & (right + 1 < len(prices)):
                    # (빨리 팔았을 때의 손실) - (쿨다운 비용) > 0 => 쿨다운 비용을 치르는 것이 나음
                    if (prices[right - 1] - prices[right - 2]) - (prices[right + 1] - prices[right]) > 0:
                        sumProfit += currentProfit
                        left = right + 1
                        right = left + 1
                    else:
                        sumProfit += currentProfit - (prices[right - 1] - prices[right - 2])
                        left = right
                        right = left + 1
                    currentProfit = 0
                else:
                    sumProfit += currentProfit
                    left = right
                    right += 1

        return sumProfit










