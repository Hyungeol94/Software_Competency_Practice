#https://leetcode.com/problems/apply-operations-to-maximize-score/submissions/1590079388/?envType=daily-question&envId=2025-03-29
#2818. Apply Operations to Maximize Score

class Solution:
    def get_score(self, num):
        score = 0
        factor = 2
        while factor * factor <= num:
            if num % factor == 0:
                score += 1
                while num % factor == 0:
                    num //= factor
            factor += 1
        if num > 1:
            score += 1
        return score

    def maximumScore(self, nums: List[int], k: int) -> int:
        scores = []
        for num in nums:
            scores.append(self.get_score(num))

        #정렬.. 제일 큰 것부터 찾아나가면서 채워넣기
        arr = sorted([(num, i) for i, num in enumerate(nums)], key= lambda a: -a[0])
        #몇개까지 가능한지 찾기
        i = 0
        answer = 1
        n = len(nums)
    
        mystack = []
        leftIndices = [] #현재 스코어에 해당하는 넘버를 유지할 수 있게 하는 것들
        for i in range(n):
            while mystack and scores[mystack[-1]] < scores[i]: #더 커야만 현재 넘버를 유지할 수 있음
                mystack.pop()
            if not mystack:
                leftIndices.append(-1)
            else:
                leftIndices.append(mystack[-1])
            mystack.append(i)
        
        mystack = []
        rightIndices = []
        
        for i in range(n-1, -1, -1):
            while mystack and scores[mystack[-1]] <= scores[i]: #더 크거나 같아야 현재 넘버를 유지할 수 있음
                mystack.pop()
            if not mystack:
                rightIndices.append(n)
            else:
                rightIndices.append(mystack[-1])
            mystack.append(i)
        rightIndices = rightIndices[::-1]

        while 0 < k:
            num, idx = arr[i] #제일 포텐이 큰 것 먼저
            #이 값을 어떻게 유지할 수 있을까요?
            count1 = idx-leftIndices[idx]
            count2 = rightIndices[idx]-idx
            count = count1 * count2
            answer = (answer * pow(num, min(count, k), 10**9+7)) % (10**9+7)
            k -= min(count, k)
            i += 1
        return answer % (10**9+7)