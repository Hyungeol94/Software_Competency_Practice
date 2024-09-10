# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import defaultdict

class Solution:
    def __init__(self):
        self.primeNums = []
        for i in range(2, 5001):
            isPrime = True
            for j in self.primeNums:
                if i % j == 0:
                    isPrime = False
            if isPrime:
                self.primeNums.append(i)
    
    @cache
    def getDivisors(self, num):
        divisor_counts = defaultdict(int)

        curr = num
        for divisor in self.primeNums:
            while True:
                if curr % divisor != 0:
                    break
                if curr == 0:
                    break
                curr //= divisor
                divisor_counts[divisor] += 1
        return divisor_counts   
        
    def getGreatestCommonDivisors(self, num1, num2):
        num1_divisors = self.getDivisors(num1)
        num2_divisors = self.getDivisors(num2)
        common_divisors = set(num1_divisors.keys()) & set(num2_divisors.keys())
        answer = 1
        for divisor in list(common_divisors):
            answer *= divisor ** min(num1_divisors[divisor], num2_divisors[divisor])
        return answer

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        curr = head.next
        while curr:
            greatest_common_divisor = self.getGreatestCommonDivisors(prev.val, curr.val)
            prev.next = ListNode(greatest_common_divisor)
            prev.next.next = curr
            prev = curr
            curr = curr.next
        return head