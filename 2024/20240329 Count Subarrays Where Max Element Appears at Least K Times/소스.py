#https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/?envType=daily-question&envId=2024-03-29
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        self.nums = nums
        self.k = k
        n = len(nums)
        left = 0
        self.maxNum = max(nums)
        self.indices = []
        for i, num in enumerate(nums):
            if num == self.maxNum:
                self.indices.append(i)
        
        if len(self.indices) < k:
            return 0
     

        self.countSum = [0]*len(nums)
        self.countSum[0] = 1 if nums[0] == self.maxNum else 0
        for i in range(1, len(self.countSum)):
            self.countSum[i] = self.countSum[i-1]+1 if nums[i] == self.maxNum else self.countSum[i-1]
        
        count = 0
        left = 0

        #left를 계속 움직이기
        #left로부터 maxNum이 k번째 등장하는 인덱스를 구하기
        #그 인덱스로부터 끝 인덱스까지의 거리를 구해서 count에 더하기

        count = 0    
        for left, _ in enumerate(self.countSum):
            i = self.get_index_of_kth_appearance(left)
            count += n-i
        return count

    def get_index_of_kth_appearance(self, left):
        if left == 0:
            for i, countSum in enumerate(self.countSum):
                if countSum == self.k:
                    return i
        
        for i, countSum in enumerate(self.countSum):
            if countSum-self.countSum[left-1] == self.k:
                return i
        return len(self.countSum)
    
        
        


        


        
        