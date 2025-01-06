#https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/
#1769. Minimum Number of Operations to Move All Balls to Each Box
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        #init
        left_count = 0
        right_count = boxes.count("1")
        answer = []
        
        acc = 0
        for i, bit in enumerate(boxes):
            if bit == "1":
                acc += (i+1)
    
        #operation
        for i, bit in enumerate(boxes):
            acc -= right_count
            acc += left_count
            answer.append(acc)

            if bit == "1":
                right_count -= 1
                left_count += 1

        return answer