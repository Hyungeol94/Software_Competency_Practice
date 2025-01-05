class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        acc = [0]*len(s)
        for shift in shifts:
            start, end, dr = shift
            for i in range(start, end+1):
                acc[i] = acc[i]+1 if dr == 1 else acc[i]-1
        
        arr = [c for c in s]

        for i, _ in enumerate(acc):
            c = arr[i]
            pos = ord(c) + acc[i]
            if not ord("a") <= pos <= ord("z"):
                pos = pos % (ord("z")+1) + ord("a")
            arr[i] = chr(pos)
        return "".join(arr)