class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        p1 = 0
        p2 = 0
        #t와 s간의 longest common subsequence를 구하기
        lcs = '' 
        while p1!=len(s) and p2!=len(t):
            if p1 == len(s):
                break
            if p2 == len(t):
                break

            if s[p1] == t[p2]:
                lcs += t[p2]
                p2 += 1 #p2 인덱스를 옮기기 
            p1 += 1 #t의 p2 인덱스에 있는 문자와 동일한 문자가 있는 s의 인덱스까지 p1을 옮기기
        return len(t) - len(lcs)
