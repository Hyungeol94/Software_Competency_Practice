import bisect

class Solution:
    def __init__(self):
        self.maxLen = 0

    def dfs(self, arr, i, mystack):
        if 2 < len(mystack): 
            self.maxLen = max(len(mystack), self.maxLen)

        if len(mystack) < 2:
            for j in range(i, len(arr)):
                mystack.append(arr[j])
                self.dfs(arr, j+1, mystack)
                mystack.pop()
        
        else:
            index = bisect.bisect_left(arr, mystack[-2]+mystack[-1])
            if index < len(arr) and arr[index] == mystack[-2]+mystack[-1]:
                mystack.append(arr[index])
                self.dfs(arr, index, mystack)
                mystack.pop()
        

    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        #일단 dfs -> 조건적으로 쌓기
        mystack = []
        self.dfs(arr, 0, mystack)
        return self.maxLen