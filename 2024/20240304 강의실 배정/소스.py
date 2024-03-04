from collections import deque
class Solution:
    def __init__(self):
        self.N = int(input())
        self.times = []
        for _ in range(self.N):
            s, t = map(int, input().split())
            self.times.append([s, t])
        # 끝나는 시간을 기준으로 정렬
        self.times.sort(key = lambda a:a[0])
        self.times = deque(self.times)

    def minClassroom(self):
        maxNum = -float('inf')
        i = 0
        #각 타임마다 겹치는 게 몇 개인지만 트래킹하기
        if len(self.times) == 1:
            return 1
        left = 0 #top index
        right = 1 #bottom index
        #sliding window
        top_s, top_t = self.times[left]
        bottom_s, bottom_t = self.times[right]
        command = "expand"
        count = 1 if top_t > bottom_s else 0
        maxNum = 1
        while right != len(self.times):
            top_s, top_t = self.times[left]
            bottom_s, bottom_t = self.times[right]
            if top_t > bottom_s:
                count += 1
                maxNum = max(maxNum, count)
                right += 1
            else:
                left += 1
                count = count-1 if count > 1 else 1
                if left == right:
                    right += 1

        print(maxNum)

instance = Solution()
instance.minClassroom()






