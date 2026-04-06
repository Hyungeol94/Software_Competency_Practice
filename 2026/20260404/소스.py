#https://leetcode.com/problems/decode-the-slanted-ciphertext/description/?envType=daily-question&envId=2026-04-04
#1324. Decode the Slanted Ciphertext

class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        col_length = len(encodedText) // rows
        matrix = []
        for i in range(rows):
            matrix.append(encodedText[col_length*i:col_length*(i+1)])
        n, m = rows, col_length

        arr = []
        for j in range(m):
            pos = [0, j]
            temp = []
            while 0 <= pos[0] < n and 0 <= pos[1] < m:
                temp.append(matrix[pos[0]][pos[1]])
                pos[0] += 1
                pos[1] += 1
            arr.append("".join(temp))
        
        text = "".join(arr)
        i = -1
        while abs(i) <= len(text) and text[i] == " ":
            i -= 1
        
        return text[:i+1] if i != -1 else text