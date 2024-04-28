from collections import defaultdict
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        #모든 노드에서 dfs를 하기? 당연히 안되겠지 .. 
        # dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5) + ... + dist(0, n)
        #dist(1,2) + dist(1,3) + dist(1,4) + dist(1,5) + ... + dist(1, n)
        
        #Hierholzer 알고리즘. 스택을 쌓아가기. 막다른곳 만나면 백트래킹 하면서 길이 업데이트 하기. 
        #문제 재정의. 이제 한 줄기 안에서 각각의 노드끼리의 길이 구하기. 조합을 구하는 이중포문으로 가능.
        #한 점으로부터 각각 한 다음에 채워지지 않은 곳끼리는 원점까지의 거리를 각각 더하기.
        
        adjList = defaultdict(list)
        dp = [[float('inf')]*n for _ in range(n)]
        
        for k, v in edges:
            adjList[k].append(v)
            adjList[v].append(k)
            dp[k][v] = 1
            dp[v][k] = 1
        
        visited = set()  
        self.mystack = [0]
        visited.add(0)

        def dfs():
            curr = self.mystack[-1]
            if len(adjList[curr]) == 1: #막다른길에 들어옴
                for i in range(len(self.mystack)-1):
                    for j in range(i+1, len(self.mystack)):
                        dp[self.mystack[i]][self.mystack[j]] = abs(i-j)
                        dp[self.mystack[j]][self.mystack[i]] = abs(i-j)
        
            else:
                for node in adjList[curr]:
                    if node not in visited:
                        self.mystack.append(node)
                        visited.add(node)
                        dfs()
                        self.mystack.pop()

        dfs()
        #최소 부모 노드의 길이만큼 더하기
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if dp[i][j] == float('inf'):
                    minNum = float('inf')
                    for k in range(n):
                        minNum = min(minNum, dp[i][k]+dp[k][j])
                    dp[i][j] = minNum
                    dp[j][i] = minNum
        

        for i in range(n):
            dp[i][i] = 0
                
        answer = []
        for i in range(n):
            answer.append(sum(dp[i]))

        return answer

