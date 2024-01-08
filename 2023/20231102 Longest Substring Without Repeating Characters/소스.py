class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        left = 0
        right = 0
        max_length = 1
        command = "expand"
        char_dict = {s[0]:1}
        #sliding window 방식으로 구현하기
        while left != len(s)-1:                       
            next_char = s[right+1] if right < len(s)-1 else s[right]              
            if command == "expand":                  
                if char_dict.get(next_char): #overlap
                    command = "shrink"
                    continue
                if right < len(s)-1:
                    right += 1 
                else:
                    command = "shrink"
                    continue
                char_dict[next_char] = 1
                max_length = max(max_length, right-left+1)

            elif command == "shrink":
                char_dict.pop(s[left])
                left += 1
                if not char_dict.get(next_char):
                    command = "expand"
                    continue
        return max_length
