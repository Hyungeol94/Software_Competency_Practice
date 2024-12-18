class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = []
        n = len(prices)
        for i, price in enumerate(prices):
            j = i+1
            is_found = False
            while j < n:
                if prices[j] <= price:
                    answer.append(price-prices[j])
                    is_found = True
                    break
                j+=1
            if not is_found:
                answer.append(price)
        
        return answer