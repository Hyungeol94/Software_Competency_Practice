class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        commands = []
        j = 0
        targetEndIndex = len(target)-1
        if n == 0 or not target:
            return []
        for e in range(1, n+1):            
            if j == targetEndIndex+1:
                break
            if e == target[j]:
                commands.append('Push')
                j+= 1 
                continue
            elif e < target[j]:
                commands.append('Push')
                commands.append('Pop')                
                continue
            
        return commands