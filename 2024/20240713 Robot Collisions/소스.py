from collections import deque

class Solution:
    def collision(self, r1, r2):
        #position, health, direction
        health = 1
        if r1[health] == r2[health]:
            return None
        
        if r1[health] > r2[health]:
            return (r1[0], r1[1]-1, r1[2], r1[3])
        
        else:
            return (r2[0], r2[1]-1, r2[2], r2[3])


    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:

        robots = list(zip(positions, healths, directions, list(range(len(positions)))))
        robots.sort()
        robots = deque(robots)
        
        mystack = []
        while robots:
            robot = robots.popleft()
            position, health, direction, i = robot
            if direction == 'L':
                if mystack and mystack[-1][2] == 'R': ##collision
                    prev = mystack.pop()
                    result = self.collision(prev, robot)
                    if not result:
                        continue
                    robots.appendleft(result)
                else:
                    mystack.append(robot)
            
            else:
                mystack.append(robot)
        
        mystack.sort(key = lambda a: a[3])
        return [item[1] for item in mystack]
        print(mystack)