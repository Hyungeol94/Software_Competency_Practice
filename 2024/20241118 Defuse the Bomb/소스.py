class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        #prefix sum 챙기기
        arr = []
        acc = 0
        for num in code:
            acc += num
            arr.append(acc)
        
        n = len(code)

        for i, _ in enumerate(code):
            #edge case
            if k == 0:
                code[i] = 0
                continue
            elif k > 0:
                start = i
                end = (i+k) % n
                code[i] = arr[end]-arr[start] if i+k < n else arr[n-1]-arr[start] + arr[end]   
            else: 
                start = (i-1) % n
                end = (i+k-1) % n
                code[i] = (arr[start]-arr[end]) if 0 <= i+k-1 else (arr[n-1]-arr[end] + (arr[start] if start != n-1 else 0))
        
        return code