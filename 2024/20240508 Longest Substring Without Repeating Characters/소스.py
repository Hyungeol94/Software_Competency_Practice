class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        charSet = set()
        maxLen = 1
        left = 0
        right = 1
        charSet.add(s[0])

        while right < len(s):
            c = s[right]
            if c in charSet:
                charSet.remove(s[left])
                left += 1

            else:
                charSet.add(c)
                maxLen = max(maxLen, right-left+1)
                right += 1

        return maxLen

