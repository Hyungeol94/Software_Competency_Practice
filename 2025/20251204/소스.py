#https://leetcode.com/problems/count-collisions-on-a-road/?envType=daily-question&envId=2025-12-04
#2211. Count Collisions on a Road

class Solution:
    def countCollisions(self, directions: str) -> int:
        mystack = []
        num_collisions = 0
        for direction in directions:
            if not mystack: 
                mystack.append(direction)
                continue
            top = mystack[-1]
            if direction == 'L':
                if top == 'R':
                    while mystack and mystack[-1] == 'R':
                        num_collisions += 1
                        mystack.pop()
                    num_collisions += 1
                    mystack.append('S')
                elif top == 'S':
                    num_collisions += 1
                    mystack[-1] = 'S'
                else:
                    mystack.append('L')
            elif direction == 'S':
                if top == 'R':
                    while mystack and mystack[-1] == 'R':
                        num_collisions += 1
                        mystack.pop()
                mystack.append(direction)

            else: #direction == 'R'
                mystack.append(direction)

        return num_collisions