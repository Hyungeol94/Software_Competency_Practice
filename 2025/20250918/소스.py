#https://leetcode.com/problems/design-task-manager/description/?envType=daily-question&envId=2025-09-18
#3408. Design Task Manager

import heapq

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_map = {}
        self.heap = []
        heapq.heapify(self.heap)

        for user_id, task_id, priority, in tasks:
            self.task_map[task_id] = (priority, user_id)
            heapq.heappush(self.heap, (-priority, -task_id))
        

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_map[taskId] = (priority, userId)
        heapq.heappush(self.heap, (-priority, -taskId))


    def edit(self, taskId: int, newPriority: int) -> None:
        _, user_id = self.task_map[taskId]
        self.task_map[taskId] = (newPriority, user_id)
        heapq.heappush(self.heap, (-newPriority, -taskId))


    def rmv(self, taskId: int) -> None:
        del self.task_map[taskId]

        
    def execTop(self) -> int:
        while self.heap:
            curr = heapq.heappop(self.heap)
            top_priority, task_id = -curr[0], -curr[1]
            if not self.task_map.get(task_id):
                continue
            priority, user_id = self.task_map[task_id]
            if priority != top_priority: #check if priority is stale
                continue
            del self.task_map[task_id]
            return user_id
        return -1
            

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()