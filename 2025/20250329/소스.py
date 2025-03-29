#https://leetcode.com/problems/apply-operations-to-maximize-score/submissions/1590079388/?envType=daily-question&envId=2025-03-29
#2818. Apply Operations to Maximize Score

class Solution:
    def get_score(self, num, prime_nums):
        #소인수분해 후, 점수 반환
        curr = num
        i = 0
        score = 0
        while curr != 1:
            prime_num = prime_nums[i]
            if curr % prime_num == 0:
                score += 1
                while curr % prime_num == 0:
                    curr = curr // prime_num
            i += 1
        return score

    def maximumScore(self, nums: List[int], k: int) -> int:
        #에라스토스테네스의 채로 소인수분해 재료 구하기
        prime_nums = []
        candidates = [True]*100000
        for i in range(2, 100000):
            if candidates[i] == True:
                prime_nums.append(i)
                for j in range(i, 100000, i):
                    candidates[j] = False
        
        scores = []
        for num in nums:
            scores.append(self.get_score(num, prime_nums))

        #정렬.. 제일 큰 것부터 찾아나가면서 채워넣기
        arr = sorted([(num, i) for i, num in enumerate(nums)], key= lambda a: -a[0])
        #몇개까지 가능한지 찾기
        print(scores)
        i = 0
        answer = 1
        while 0 < k:
            num, idx = arr[i] #제일 포텐이 큰 것 먼저
            #이 값을 어떻게 유지할 수 있을까요?
            curr_score = scores[idx]
            base = curr_score
            count1 = 0
            j = idx-1
            while 0 <= j:
                if scores[j] < base:
                    j -= 1
                else:
                    break
            count1 = idx-j

            j = idx
            while j < len(scores):
                if scores[j] <= base:
                    j += 1
                else:
                    break
            count2 = j-idx
            count = count1 * count2
            # print(count1, count2)
            answer = (answer * pow(num, min(count, k), 10**9+7)) % (10**9+7)
            k -= min(count, k)
            i += 1
        return answer % (10**9+7)            