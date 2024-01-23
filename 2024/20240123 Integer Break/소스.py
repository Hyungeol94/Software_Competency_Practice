#https://leetcode.com/problems/integer-break

class Solution:
    def getMaximumProduct(self, n):
        maximumProduct = -float('inf')
        for i in range(1, n//2+1):
            maximumProduct = max(maximumProduct, max(i, self.maximumProducts[i])*max(n-i, self.maximumProducts[n-i]))
        return maximumProduct
            

    def integerBreak(self, n: int) -> int:
        self.maximumProducts = [-float('inf') if 3<=i else 1 for i in range(n+1)]
        for i in range(3, n+1):
            self.maximumProducts[i] = self.getMaximumProduct(i)
        return self.maximumProducts[n]

            
        

                    



        

        
        