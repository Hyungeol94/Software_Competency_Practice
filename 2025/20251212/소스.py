#https://leetcode.com/problems/count-mentions-per-user/?envType=daily-question&envId=2025-12-12
#3433. Count Mentions Per User

from collections import deque

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        mentions = [0 for _ in range(numberOfUsers)]
        is_online = [True for _ in range(numberOfUsers)]
        sorted_events = sorted(events, key = lambda a: (int(a[1]), -ord(a[0][0])))

        myqueue = deque([])
        for event in sorted_events:
            event_type, time, _ = event
            while myqueue and myqueue[0][1] <= int(time):
                user_id = myqueue[0][0]
                is_online[user_id] = True
                myqueue.popleft()
            if event_type == "OFFLINE":
                user_id = int(event[2])
                is_online[user_id] = False
                myqueue.append((user_id, int(time)+60))
            elif event_type == "MESSAGE":
                mentions_string = event[2]
                if mentions_string == "ALL":
                    mentions = [count+1 for count in mentions]
                elif mentions_string == "HERE":
                    mentions = [count+1 if is_online[i] else count for i, count in enumerate(mentions)]
                else:
                    ids = mentions_string.split()
                    for user_id in ids:
                        mentions[int(user_id[2:])] += 1
        
        return mentions