class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefixes = []
        prefix = 1

        for num in nums:
            if num == 0:
                prefix = 1
                prefixes.append(num)
                continue
            prefix *= num
            prefixes.append(prefix)

        #마이너스 숫자의 개수 의 홀수 정보를 담고 있는 마스크가 필요함
        maxVal = -float('inf')
        mydict = dict()
        mask = 0
        for i, num in enumerate(nums):
            if num == 0:
                if 0 in mydict:
                    del mydict[0] 
                if 1 in mydict:
                    del mydict[1]
                maxVal = max(maxVal, num)
                continue
                
            if num < 0:
                mask = mask ^ 1
            if mask not in mydict:
                mydict[mask] = i
            
            start_index = mydict[mask]
            end_index = i

            if start_index == end_index: 
                maxVal = max(maxVal, prefixes[i])
                continue
            
            dividend = prefixes[end_index]
            modulo = prefixes[start_index] if prefixes[start_index] else 1
            
            maxVal = max(maxVal, dividend // modulo, prefixes[end_index])

        return maxVal