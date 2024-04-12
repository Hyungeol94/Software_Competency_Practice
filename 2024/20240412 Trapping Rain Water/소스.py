#https://leetcode.com/problems/trapping-rain-water/description/

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
    
        rain = 0     
        for i, h in enumerate(height):
            if not stack:
                stack.append(h)
                continue
            
            if stack[0] <= h:
                while stack:
                    rain += stack[0]-stack.pop()
                stack =[h]
            else:
                stack.append(h)

        if stack and len(stack)!=1:
            stack = stack[::-1]
            rain += self.trap(stack)
        
        return rain