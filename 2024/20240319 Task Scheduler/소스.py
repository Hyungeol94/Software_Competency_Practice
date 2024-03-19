#https://leetcode.com/problems/task-scheduler/

class Solution:
    def coolDown(self, coolDownHash):
        for task, time in coolDownHash.items():
            coolDownHash[task] =  coolDownHash[task]-1 if coolDownHash[task] != 0 else 0

    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskHash = {}
        for task in tasks:
            taskHash[task] = taskHash[task]+1 if task in taskHash else 1

        #greedy하게 가기
        taskHash = sorted([list(i) for i in taskHash.items()], key=lambda a: -a[1])
        print(taskHash)
        coolDownHash = {}
        for task, count in taskHash:
            coolDownHash[task] = 0

        minLen = 0
        while taskHash:
            i = 0
            taskFound = False
            while i!=len(taskHash):
                task, count = taskHash[i]
                cooldown = coolDownHash[task]
                if cooldown != 0:
                    i += 1
                    continue
                taskHash[i][1] -= 1
                minLen += 1
                self.coolDown(coolDownHash)
                coolDownHash[task] = n
                if taskHash[i][1] == 0:
                    taskHash.pop(i)
                taskFound = True
                break
            if not taskFound:
                self.coolDown(coolDownHash)
                minLen += 1
            taskHash.sort(key=lambda a: -a[1])
        return minLen
                    
            
                
                

                
            
        

            
                
            

        
       
            
        
        
        

        