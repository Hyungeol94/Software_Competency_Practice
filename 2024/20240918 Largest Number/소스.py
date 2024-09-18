from collections import defaultdict

class Solution:
    def tweak_num(self, num_str, max_num):
        return (num_str * 100)[:len(max_num)*2]


    def sort_array(self, key: str, array: List[int]) -> List[int]:
        arr = [str(num) for num in array]
    
        max_num = sorted(arr, key = lambda a: -int(a))[0]

        return sorted(arr, key = lambda a: -int(self.tweak_num(a, max_num)))


    def largestNumber(self, nums: List[int]) -> str:
        my_dict = defaultdict(list)
        for num in nums:
            my_dict[str(num)[0]].append(num)
        
        answer = []
        for key, elements in sorted(list(my_dict.items()), key = lambda a: -int(a[0])):
            answer += self.sort_array(key, elements)
        
        return str(int(''.join(answer)))
            