class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            s = s[::-1]  # Reverse the string
            x, y = y, x
        
        def remove_substring(s, pattern, points):
            stack = []
            score = 0
            for char in s:
                if stack and stack[-1] + char == pattern:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)
            return ''.join(stack), score

        # First pass: remove higher value pattern
        remaining_s, score = remove_substring(s, "ab", x)
        # Second pass: remove the other pattern
        _, score2 = remove_substring(remaining_s, "ba", y)

        return score + score2

# Example usage:
sol = Solution()
result = sol.maximumGain("ababbab", 3, 4)
print(result)  # Output will be the maximum gain